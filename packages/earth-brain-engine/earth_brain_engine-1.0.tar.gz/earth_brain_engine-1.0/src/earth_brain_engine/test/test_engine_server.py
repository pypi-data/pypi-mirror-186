# -* -coding: UTF-8 -* -
"""pytest"""

from earth_brain_engine import Task, Model


def test_create_engine_task():
    args = {"dataset_root": "/home/nfs/appnfs/ggx001/jobs/data-center-20230104-095947-0xca64/VOC"}
    engine = Task(name="目标检测faster_rcnn_resnet50", version="1.0.0")
    data = engine.create(**args)
    assert isinstance(data, dict)


def test_get_engine_status():
    args = {'sql_id': 34}
    engine = Task(name="目标检测faster_rcnn_resnet50", version="1.0.0")
    data = engine.status(**args)
    assert isinstance(data, dict)


def test_get_task_log():
    args = {'sql_id': 34}
    data = Task.log(**args)
    print(data)


def test_get_task_event():
    args = {'sql_id': 34}
    data = Task.event(**args)
    assert isinstance(data, list)


def test_aborted_task():
    args = {'sql_id': 35}
    data = Task.abort(**args)
    assert isinstance(data, str)


def test_deleted_task():
    args = {'sql_id': 35}
    data = Task.delete(**args)
    assert isinstance(data, str)


def test_predict_model_server():
    engine = Model(name="zws-mindspore-file", version='1.2.3')
    import base64
    img_file = '/Users/liudonggang/Desktop/Study/Data/Airport/airport_332.jpg'
    with open(img_file, 'rb') as fr:
        image_b64 = str(base64.b64encode(fr.read()), "utf-8")
    args = {"instances": [{"image": {"b64": image_b64}}]}
    data = engine.predict(**args)
    print(data)
    assert isinstance(data, dict)


if __name__ == '__main__':
    test_get_task_log()
