from tasks import Task
def test_dict():
        task = Task('do something', 'okken', True, 21)
        dict = task._asdict()
        expected = {'summary': 'do something',
                    'owner': 'okken',
                    'done': True,
                    'id': 21}
        assert dict == expected
