import pytest
from slapping.slap_that_like_button import LikeState, slap_many


def test_empty_slap():
    assert slap_many(LikeState.empty, '') is LikeState.empty


def test_single_slaps():
    assert slap_many(LikeState.empty, 'l') is LikeState.liked
    assert slap_many(LikeState.empty, 'd') is LikeState.disliked


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),

])
def test_multi_slaps(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


# related to skip is skip_if where conditions can be set (ex. skip if on Windows)
@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


# If you have a test that you know is failing, but you don't want it to affect the build's outcome.
# It will still run the test (and fail), but not count as a failure for the build
# NOTE: This is different from an expected fail
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


# This test needs to raise an exception in order to be successful
def test_invalid_slap():
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, 'X')


# Fixtures (e.g. db_conn), if needed, are used to set up the environment before testing and cleaning up after
# Fixtures can be defined next to the test, but to have them available everywhere, they need to be in conftest.py

@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"


# def test_many_slaps():
#     assert slap_many(LikeState.empty, 'll') is LikeState.empty
#     assert slap_many(LikeState.empty, 'dd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert slap_many(LikeState.empty, 'dl') is LikeState.liked
#     assert slap_many(LikeState.empty, 'ldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'lldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ddl') is LikeState.liked
