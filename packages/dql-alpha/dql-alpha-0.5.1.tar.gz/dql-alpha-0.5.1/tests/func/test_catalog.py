import shutil

import pytest
import yaml

from dql.catalog import parse_dql_file
from dql.utils import remove_readonly


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_find(cloud_test_catalog):
    src = cloud_test_catalog.src
    catalog = cloud_test_catalog.catalog
    config = cloud_test_catalog.client_config

    assert set(catalog.find([str(src)], client_config=config)) == {
        str(src / "description"),
        str(src / "cats") + "/",
        str(src / "cats" / "cat1"),
        str(src / "cats" / "cat2"),
        str(src / "dogs") + "/",
        str(src / "dogs" / "dog1"),
        str(src / "dogs" / "dog2"),
        str(src / "dogs" / "dog3"),
        str(src / "dogs" / "others") + "/",
        str(src / "dogs" / "others" / "dog4"),
    }

    with pytest.raises(FileNotFoundError):
        set(
            catalog.find(
                [str(src / "does_not_exist")],
                client_config=config,
            )
        )


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_find_names_paths_size_type(cloud_test_catalog):
    src = cloud_test_catalog.src
    catalog = cloud_test_catalog.catalog
    config = cloud_test_catalog.client_config

    assert set(
        catalog.find([str(src)], names=["*cat*"], client_config=config)
    ) == {
        str(src / "cats") + "/",
        str(src / "cats" / "cat1"),
        str(src / "cats" / "cat2"),
    }

    assert set(
        catalog.find(
            [str(src)], names=["*cat*"], typ="dir", client_config=config
        )
    ) == {
        str(src / "cats") + "/",
    }

    assert (
        len(
            list(
                catalog.find([str(src)], names=["*CAT*"], client_config=config)
            )
        )
        == 0
    )

    assert set(
        catalog.find([str(src)], inames=["*CAT*"], client_config=config)
    ) == {
        str(src / "cats") + "/",
        str(src / "cats" / "cat1"),
        str(src / "cats" / "cat2"),
    }

    assert set(
        catalog.find([str(src)], paths=["*cats/cat*"], client_config=config)
    ) == {
        str(src / "cats" / "cat1"),
        str(src / "cats" / "cat2"),
    }

    assert (
        len(
            list(
                catalog.find(
                    [str(src)], paths=["*caTS/CaT**"], client_config=config
                )
            )
        )
        == 0
    )

    assert set(
        catalog.find([str(src)], ipaths=["*caTS/CaT*"], client_config=config)
    ) == {
        str(src / "cats" / "cat1"),
        str(src / "cats" / "cat2"),
    }

    assert set(
        catalog.find([str(src)], size="5", typ="f", client_config=config)
    ) == {
        str(src / "description"),
    }

    assert set(
        catalog.find([str(src)], size="-3", typ="f", client_config=config)
    ) == {
        str(src / "dogs" / "dog2"),
    }


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_find_names_columns(cloud_test_catalog):
    src = cloud_test_catalog.src
    catalog = cloud_test_catalog.catalog
    config = cloud_test_catalog.client_config

    src_str = str(src)
    owner = "webfile" if src_str.startswith("s3") else ""

    assert set(
        catalog.find(
            [src_str],
            names=["*cat*"],
            columns=["du", "name", "owner", "path", "size", "type"],
            client_config=config,
        )
    ) == {
        "\t".join(columns)
        for columns in [
            ["8", "cats", "", str(src / "cats") + "/", "0", "d"],
            ["4", "cat1", owner, str(src / "cats" / "cat1"), "4", "f"],
            ["4", "cat2", owner, str(src / "cats" / "cat2"), "4", "f"],
        ]
    }


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
@pytest.mark.parametrize(
    "recursive,star",
    ((True, True), (True, False), (False, True), (False, False)),
)
def test_cp_root(cloud_test_catalog, recursive, star):
    src = cloud_test_catalog.src
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    if star:
        src_path = f"{str(src).rstrip('/')}/*"
    else:
        src_path = str(src)

    catalog.cp(
        [src_path],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=recursive,
    )

    if not star and not recursive:
        # The root directory is skipped, so nothing is copied
        assert (dest / "description").exists() is False
        assert (dest / "cats").exists() is False
        assert (dest / "dogs").exists() is False
        assert (dest / "others").exists() is False
        assert dest.with_suffix(".dql").exists() is False
        return

    assert (dest / "description").read_text() == "Cats and Dogs"

    # Testing DQL File Contents
    assert dest.with_suffix(".dql").is_file()
    dql_contents = yaml.safe_load(dest.with_suffix(".dql").read_text())
    assert len(dql_contents) == 1
    data = dql_contents[0]
    assert data["data-source"]["uri"] == src_path.rstrip("/")
    expected_file_count = 7 if recursive else 1
    assert len(data["files"]) == expected_file_count
    files_by_name = {f["name"]: f for f in data["files"]}

    # Directories should never be saved
    assert "cats" not in files_by_name
    assert "dogs" not in files_by_name
    assert "others" not in files_by_name
    assert "dogs/others" not in files_by_name

    # Ensure all files have checksum saved
    for f in data["files"]:
        assert len(f["checksum"]) > 1

    # Description is always copied (if anything is copied)
    prefix = "" if star else "/"
    assert files_by_name[f"{prefix}description"]["size"] == 13

    if recursive:
        assert (dest / "cats" / "cat1").read_text() == "meow"
        assert (dest / "cats" / "cat2").read_text() == "mrow"
        assert (dest / "dogs" / "dog1").read_text() == "woof"
        assert (dest / "dogs" / "dog2").read_text() == "arf"
        assert (dest / "dogs" / "dog3").read_text() == "bark"
        assert (dest / "dogs" / "others" / "dog4").read_text() == "ruff"
        assert files_by_name[f"{prefix}cats/cat1"]["size"] == 4
        assert files_by_name[f"{prefix}cats/cat2"]["size"] == 4
        assert files_by_name[f"{prefix}dogs/dog1"]["size"] == 4
        assert files_by_name[f"{prefix}dogs/dog2"]["size"] == 3
        assert files_by_name[f"{prefix}dogs/dog3"]["size"] == 4
        assert files_by_name[f"{prefix}dogs/others/dog4"]["size"] == 4
        return

    assert (dest / "cats").exists() is False
    assert (dest / "dogs").exists() is False
    for prefix in ["/", ""]:
        assert f"{prefix}cats/cat1" not in files_by_name
        assert f"{prefix}cats/cat2" not in files_by_name
        assert f"{prefix}dogs/dog1" not in files_by_name
        assert f"{prefix}dogs/dog2" not in files_by_name
        assert f"{prefix}dogs/dog3" not in files_by_name
        assert f"{prefix}dogs/others/dog4" not in files_by_name


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
@pytest.mark.parametrize(
    "recursive,star,slash",
    (
        (True, True, False),
        (True, False, False),
        (True, False, True),
        (False, True, False),
        (False, False, False),
        (False, False, True),
    ),
)
def test_cp_subdir(cloud_test_catalog, recursive, star, slash):
    src = cloud_test_catalog.src / "dogs"
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    if star:
        src_path = f"{str(src)}/*"
    else:
        src_path = str(src)
        if slash:
            src_path = f"{src_path}/"

    catalog.cp(
        [src_path],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=recursive,
    )

    if not star and not recursive:
        # Directories are skipped, so nothing is copied
        assert (dest / "dog1").exists() is False
        assert (dest / "dog2").exists() is False
        assert (dest / "dog3").exists() is False
        assert (dest / "dogs").exists() is False
        assert (dest / "others").exists() is False
        assert dest.with_suffix(".dql").exists() is False
        return

    # Testing DQL File Contents
    assert dest.with_suffix(".dql").is_file()
    dql_contents = yaml.safe_load(dest.with_suffix(".dql").read_text())
    assert len(dql_contents) == 1
    data = dql_contents[0]
    assert data["data-source"]["uri"] == src_path.rstrip("/")
    expected_file_count = 4 if recursive else 3
    assert len(data["files"]) == expected_file_count
    files_by_name = {f["name"]: f for f in data["files"]}

    # Directories should never be saved
    assert "others" not in files_by_name
    assert "dogs/others" not in files_by_name

    # Ensure all files have checksum saved
    for f in data["files"]:
        assert len(f["checksum"]) > 1

    if star or slash:
        assert (dest / "dog1").read_text() == "woof"
        assert (dest / "dog2").read_text() == "arf"
        assert (dest / "dog3").read_text() == "bark"
        assert (dest / "dogs").exists() is False
        assert files_by_name["dog1"]["size"] == 4
        assert files_by_name["dog2"]["size"] == 3
        assert files_by_name["dog3"]["size"] == 4
        if recursive:
            assert (dest / "others" / "dog4").read_text() == "ruff"
            assert files_by_name["others/dog4"]["size"] == 4
        else:
            assert (dest / "others").exists() is False
            assert "others/dog4" not in files_by_name
        return

    assert (dest / "dogs" / "dog1").read_text() == "woof"
    assert (dest / "dogs" / "dog2").read_text() == "arf"
    assert (dest / "dogs" / "dog3").read_text() == "bark"
    assert (dest / "dogs" / "others" / "dog4").read_text() == "ruff"
    assert (dest / "dog1").exists() is False
    assert (dest / "dog2").exists() is False
    assert (dest / "dog3").exists() is False
    assert (dest / "others").exists() is False
    assert files_by_name["dogs/dog1"]["size"] == 4
    assert files_by_name["dogs/dog2"]["size"] == 3
    assert files_by_name["dogs/dog3"]["size"] == 4
    assert files_by_name["dogs/others/dog4"]["size"] == 4


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
@pytest.mark.parametrize(
    "recursive,star,slash",
    (
        (True, True, False),
        (True, False, False),
        (True, False, True),
        (False, True, False),
        (False, False, False),
        (False, False, True),
    ),
)
def test_cp_multi_subdir(cloud_test_catalog, recursive, star, slash):
    sources = [
        cloud_test_catalog.src / "cats",
        cloud_test_catalog.src / "dogs",
    ]
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    if star:
        src_paths = [f"{str(src)}/*" for src in sources]
    else:
        src_paths = [str(src) for src in sources]
        if slash:
            src_paths = [f"{src}/" for src in src_paths]

    catalog.cp(
        src_paths,
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=recursive,
    )

    if not star and not recursive:
        # Directories are skipped, so nothing is copied
        assert (dest / "cat1").exists() is False
        assert (dest / "cat2").exists() is False
        assert (dest / "cats").exists() is False
        assert (dest / "dog1").exists() is False
        assert (dest / "dog2").exists() is False
        assert (dest / "dog3").exists() is False
        assert (dest / "dogs").exists() is False
        assert (dest / "others").exists() is False
        assert dest.with_suffix(".dql").exists() is False
        return

    # Testing DQL File Contents
    assert dest.with_suffix(".dql").is_file()
    dql_contents = yaml.safe_load(dest.with_suffix(".dql").read_text())
    assert len(dql_contents) == 2
    data_cats = dql_contents[0]
    data_dogs = dql_contents[1]
    assert data_cats["data-source"]["uri"] == src_paths[0].rstrip("/")
    assert data_dogs["data-source"]["uri"] == src_paths[1].rstrip("/")
    assert len(data_cats["files"]) == 2
    assert len(data_dogs["files"]) == 4 if recursive else 3
    cat_files_by_name = {f["name"]: f for f in data_cats["files"]}
    dog_files_by_name = {f["name"]: f for f in data_dogs["files"]}

    # Directories should never be saved
    assert "others" not in dog_files_by_name
    assert "dogs/others" not in dog_files_by_name

    # Ensure all files have checksum saved
    for f in data_cats["files"]:
        assert len(f["checksum"]) > 1
    for f in data_dogs["files"]:
        assert len(f["checksum"]) > 1

    if star or slash:
        assert (dest / "cat1").read_text() == "meow"
        assert (dest / "cat2").read_text() == "mrow"
        assert (dest / "dog1").read_text() == "woof"
        assert (dest / "dog2").read_text() == "arf"
        assert (dest / "dog3").read_text() == "bark"
        assert (dest / "cats").exists() is False
        assert (dest / "dogs").exists() is False
        assert cat_files_by_name["cat1"]["size"] == 4
        assert cat_files_by_name["cat2"]["size"] == 4
        assert dog_files_by_name["dog1"]["size"] == 4
        assert dog_files_by_name["dog2"]["size"] == 3
        assert dog_files_by_name["dog3"]["size"] == 4
        if recursive:
            assert (dest / "others" / "dog4").read_text() == "ruff"
            assert dog_files_by_name["others/dog4"]["size"] == 4
        else:
            assert (dest / "others").exists() is False
            assert "others/dog4" not in dog_files_by_name
        return

    assert (dest / "cats" / "cat1").read_text() == "meow"
    assert (dest / "cats" / "cat2").read_text() == "mrow"
    assert (dest / "dogs" / "dog1").read_text() == "woof"
    assert (dest / "dogs" / "dog2").read_text() == "arf"
    assert (dest / "dogs" / "dog3").read_text() == "bark"
    assert (dest / "dogs" / "others" / "dog4").read_text() == "ruff"
    assert (dest / "cat1").exists() is False
    assert (dest / "cat2").exists() is False
    assert (dest / "dog1").exists() is False
    assert (dest / "dog2").exists() is False
    assert (dest / "dog3").exists() is False
    assert (dest / "others").exists() is False
    assert cat_files_by_name["cats/cat1"]["size"] == 4
    assert cat_files_by_name["cats/cat2"]["size"] == 4
    assert dog_files_by_name["dogs/dog1"]["size"] == 4
    assert dog_files_by_name["dogs/dog2"]["size"] == 3
    assert dog_files_by_name["dogs/dog3"]["size"] == 4
    assert dog_files_by_name["dogs/others/dog4"]["size"] == 4


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_cp_double_subdir(cloud_test_catalog):
    src = cloud_test_catalog.src / "dogs" / "others"
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    src_path = f"{str(src)}/"

    catalog.cp(
        [src_path],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=True,
    )

    # Testing DQL File Contents
    assert dest.with_suffix(".dql").is_file()
    dql_contents = yaml.safe_load(dest.with_suffix(".dql").read_text())
    assert len(dql_contents) == 1
    data = dql_contents[0]
    assert data["data-source"]["uri"] == src_path.rstrip("/")
    assert len(data["files"]) == 1
    files_by_name = {f["name"]: f for f in data["files"]}

    # Directories should never be saved
    assert "others" not in files_by_name
    assert "dogs/others" not in files_by_name

    # Ensure all files have checksum saved
    for f in data["files"]:
        assert len(f["checksum"]) > 1

    assert (dest / "dogs").exists() is False
    assert (dest / "others").exists() is False
    assert (dest / "dog4").read_text() == "ruff"
    assert files_by_name["dog4"]["size"] == 4


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_cp_dql_file_options(cloud_test_catalog):
    src = cloud_test_catalog.src / "dogs"
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    src_path = str(src / "*")

    dql_file = working_dir / "custom_name.dql"

    catalog.cp(
        [src_path],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=False,
        dql_only=True,
        dql_file=str(dql_file),
    )

    assert (dest / "dog1").exists() is False
    assert (dest / "dog2").exists() is False
    assert (dest / "dog3").exists() is False
    assert (dest / "dogs").exists() is False
    assert (dest / "others").exists() is False
    assert dest.with_suffix(".dql").exists() is False

    # Testing DQL File Contents
    assert dql_file.is_file()
    dql_contents = yaml.safe_load(dql_file.read_text())
    assert len(dql_contents) == 1
    data = dql_contents[0]
    assert data["data-source"]["uri"] == src_path.rstrip("/")
    expected_file_count = 3
    assert len(data["files"]) == expected_file_count
    files_by_name = {f["name"]: f for f in data["files"]}

    assert parse_dql_file(str(dql_file)) == dql_contents

    # Directories should never be saved
    assert "others" not in files_by_name
    assert "dogs/others" not in files_by_name

    assert files_by_name["dog1"]["size"] == 4
    assert files_by_name["dog2"]["size"] == 3
    assert files_by_name["dog3"]["size"] == 4
    assert "others/dog4" not in files_by_name

    with pytest.raises(FileNotFoundError):
        # Should fail, as * will not be expanded
        catalog.cp(
            [src_path],
            str(dest),
            client_config=cloud_test_catalog.client_config,
            recursive=False,
            dql_only=True,
            dql_file=str(dql_file),
            no_glob=True,
        )

    # Should succeed, as the DQL file exists check will be skipped
    dql_only_data = catalog.cp(
        [src_path],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=False,
        dql_only=True,
        dql_file=str(dql_file),
        no_dql_file=True,
    )

    # Check the returned DQL data contents
    assert len(dql_only_data) == len(dql_contents)
    dql_only_source = dql_only_data[0]
    assert dql_only_source["data-source"]["uri"] == src_path.rstrip("/")
    assert dql_only_source["files"] == data["files"]


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_cp_dql_file_sources(cloud_test_catalog):
    sources = [
        f"{str(cloud_test_catalog.src / 'cats')}/",
        str(cloud_test_catalog.src / "dogs" / "*"),
    ]
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    dql_files = [
        working_dir / "custom_cats.dql",
        working_dir / "custom_dogs.dql",
    ]

    catalog.cp(
        sources[:1],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=True,
        dql_only=True,
        dql_file=str(dql_files[0]),
    )

    catalog.cp(
        sources[1:],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=True,
        dql_only=True,
        dql_file=str(dql_files[1]),
    )

    # Files should not be copied yet
    assert (dest / "cat1").exists() is False
    assert (dest / "cat2").exists() is False
    assert (dest / "cats").exists() is False
    assert (dest / "dog1").exists() is False
    assert (dest / "dog2").exists() is False
    assert (dest / "dog3").exists() is False
    assert (dest / "dogs").exists() is False
    assert (dest / "others").exists() is False

    # Testing DQL File Contents
    dql_data = []
    for dqf in dql_files:
        assert dqf.is_file()
        dql_contents = yaml.safe_load(dqf.read_text())
        assert len(dql_contents) == 1
        dql_data.extend(dql_contents)

    assert len(dql_data) == 2
    data_cats1 = dql_data[0]
    data_dogs1 = dql_data[1]
    assert data_cats1["data-source"]["uri"] == sources[0].rstrip("/")
    assert data_dogs1["data-source"]["uri"] == sources[1].rstrip("/")
    assert len(data_cats1["files"]) == 2
    assert len(data_dogs1["files"]) == 4
    cat_files_by_name1 = {f["name"]: f for f in data_cats1["files"]}
    dog_files_by_name1 = {f["name"]: f for f in data_dogs1["files"]}

    # Directories should never be saved
    assert "others" not in dog_files_by_name1
    assert "dogs/others" not in dog_files_by_name1

    assert cat_files_by_name1["cat1"]["size"] == 4
    assert cat_files_by_name1["cat2"]["size"] == 4
    assert dog_files_by_name1["dog1"]["size"] == 4
    assert dog_files_by_name1["dog2"]["size"] == 3
    assert dog_files_by_name1["dog3"]["size"] == 4
    assert dog_files_by_name1["others/dog4"]["size"] == 4

    # Copy using these DQL files as sources
    catalog.cp(
        [str(dqf) for dqf in dql_files],
        str(dest),
        client_config=cloud_test_catalog.client_config,
        recursive=True,
    )

    # Files should now be copied
    assert (dest / "cat1").read_text() == "meow"
    assert (dest / "cat2").read_text() == "mrow"
    assert (dest / "dog1").read_text() == "woof"
    assert (dest / "dog2").read_text() == "arf"
    assert (dest / "dog3").read_text() == "bark"
    assert (dest / "others" / "dog4").read_text() == "ruff"

    # Testing DQL File Contents
    assert dest.with_suffix(".dql").is_file()
    dql_contents = yaml.safe_load(dest.with_suffix(".dql").read_text())
    assert len(dql_contents) == 2
    data_cats2 = dql_contents[0]
    data_dogs2 = dql_contents[1]
    assert data_cats2["data-source"]["uri"] == sources[0].rstrip("/")
    assert data_dogs2["data-source"]["uri"] == sources[1].rstrip("/")
    assert len(data_cats2["files"]) == 2
    assert len(data_dogs2["files"]) == 4
    cat_files_by_name2 = {f["name"]: f for f in data_cats2["files"]}
    dog_files_by_name2 = {f["name"]: f for f in data_dogs2["files"]}

    # Ensure all files have checksum saved
    for f in data_cats2["files"]:
        assert len(f["checksum"]) > 1
    for f in data_dogs2["files"]:
        assert len(f["checksum"]) > 1

    # Directories should never be saved
    assert "others" not in dog_files_by_name2
    assert "dogs/others" not in dog_files_by_name2

    assert cat_files_by_name2["cat1"]["size"] == 4
    assert cat_files_by_name2["cat2"]["size"] == 4
    assert dog_files_by_name2["dog1"]["size"] == 4
    assert dog_files_by_name2["dog2"]["size"] == 3
    assert dog_files_by_name2["dog3"]["size"] == 4
    assert dog_files_by_name2["others/dog4"]["size"] == 4


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_get(cloud_test_catalog):
    src = cloud_test_catalog.src
    catalog = cloud_test_catalog.catalog
    config = cloud_test_catalog.client_config
    dest = cloud_test_catalog.working_dir / "data"

    catalog.get(str(src), str(dest), client_config=config)

    assert (dest / "cats" / "cat1").read_text() == "meow"
    assert (dest / "cats" / "cat2").read_text() == "mrow"
    assert (dest / "dogs" / "dog1").read_text() == "woof"
    assert (dest / "dogs" / "dog2").read_text() == "arf"
    assert (dest / "dogs" / "dog3").read_text() == "bark"
    assert (dest / "dogs" / "others" / "dog4").read_text() == "ruff"
    assert dest.with_suffix(".dql").is_file()


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_get_subdir(cloud_test_catalog):
    src = f"{str(cloud_test_catalog.src)}/dogs"
    working_dir = cloud_test_catalog.working_dir
    catalog = cloud_test_catalog.catalog

    dest = working_dir / "data"

    catalog.get(src, str(dest), client_config=cloud_test_catalog.client_config)

    assert dest.with_suffix(".dql").is_file()
    assert (dest / "dog1").read_text() == "woof"
    assert (dest / "dog2").read_text() == "arf"
    assert (dest / "dog3").read_text() == "bark"
    assert (dest / "dogs").exists() is False
    assert (dest / "others" / "dog4").read_text() == "ruff"

    assert parse_dql_file(str(dest.with_suffix(".dql"))) == [
        yaml.safe_load(dest.with_suffix(".dql").read_text())
    ]

    with pytest.raises(RuntimeError):
        # An error should be raised if the output directory already exists
        catalog.get(
            src, str(dest), client_config=cloud_test_catalog.client_config
        )

    shutil.rmtree(dest, onerror=remove_readonly)
    assert dest.with_suffix(".dql").is_file()

    with pytest.raises(RuntimeError):
        # An error should also be raised if the dataset file already exists
        catalog.get(
            src, str(dest), client_config=cloud_test_catalog.client_config
        )


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_du(cloud_test_catalog):
    src = str(cloud_test_catalog.src)
    catalog = cloud_test_catalog.catalog

    expected_results = [
        (f"{src}cats/", 8),
        (f"{src}dogs/others/", 4),
        (f"{src}dogs/", 15),
        (src, 36),
    ]

    results = catalog.du([src], client_config=cloud_test_catalog.client_config)

    assert list(results) == expected_results[3:]

    results = catalog.du(
        [src], client_config=cloud_test_catalog.client_config, depth=1
    )

    assert list(results) == expected_results[:1] + expected_results[2:]

    results = catalog.du(
        [src], client_config=cloud_test_catalog.client_config, depth=5
    )

    assert list(results) == expected_results


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_ls_glob(cloud_test_catalog):
    src = cloud_test_catalog.src
    catalog = cloud_test_catalog.catalog

    assert [
        (source.node.name, [n.name for n in nodes])
        for source, nodes in catalog.ls(
            [str(src / "dogs" / "dog*")],
            client_config=cloud_test_catalog.client_config,
        )
    ] == [("dog1", ["dog1"]), ("dog2", ["dog2"]), ("dog3", ["dog3"])]
