"""A module for creating pptx from Nanofootball server request 

use create_pptx(...) for real data
or create_from_test_data(...)

Example 1:
----------
    import nf_presentation

    # для тренировки
    pptx_bytes= nf_presentaion.from_training(input_data=training_data_dict)
    # или для одного упражнения
    pptx_bytes= nf_presentaion.from_single_exercise(input_data=exercise_data_dict)
"""

import json
import io
from typing import Union,IO

from .report_renderer import ReportRenderer
from nf_presentation.renderers.compact_renderer import CompactRenderer,RenderOptions
from .data_classes import TrainingInfo
from . import assets
from nf_presentation.logger import logger


def return_bytes(func):
    """a decorator that reads the created file objects and returns a bytes array to function standart return """
    def callee(*args,output_file:Union[str,None] =  None,**kwargs):
        #target_stream= output_file or io.BytesIO()

        with io.BytesIO() as stream:

            func(*args,**kwargs,output_file=stream)

            stream.seek(0)
            data=stream.read()
            stream.close()

            if output_file is not None:
                with open(output_file,'wb') as f:
                    f.write(data)

            return data
    return callee

@return_bytes
def from_training(input_data:dict,output_file:Union[str,None] =  None):
    """A function creating a pptx file from giant dict request from Nanofootball server
    Arguments:
        input_data: dict
            'test' - use a test data(2 exercises)
            'test-long' - use a long test data(6 exercises)
            a dict-like object containing server request for making a pptx file
        output_file: str|None
            a destination for rendering pptx, may be a string for saving locally,
            

    Output:
        Byte-array 
            returns a bytes of pptx document. This data can be written to file or be send over http
    """
    if input_data=='test':
        with assets.get_test_data() as f:
            input_data=json.load(f)
    elif input_data=='test-long':
        with assets.get_test_data(short=False) as f:
            input_data=json.load(f)

    t=TrainingInfo(data=input_data)
    with ReportRenderer() as renderer:
        renderer.add_title_slide(name=t.trainer_name)
        for exercise in t.exercises:
            logger.debug(f'rendering {exercise.name}')
            renderer.add_exercise_slide(exercise=exercise)
        renderer.save(to=output_file)

@return_bytes
def from_single_exercise(input_data : Union[dict,str], render_options: dict , output_file : Union[str,None]= None) -> bytes:
    """A function creating a pptx file from exercise object in Nanofootball API
    Arguments:
        input_data: dict | str
            'test' - use a test data
            dict - a dict-like object containing server request for making a pptx file
        output_file: str|None
            a destination for rendering pptx, may be a string for saving locally,
        render_options: dict
            a set of items to show or not show on the rendered scheme
                ex. {
                scheme_1=True,
                scheme_2=True,
                scheme_1_old=True
                scheme_2_old=True,
                video_1=True,
                ...
                }

    Output:
        Byte-array 
            returns a bytes of pptx document. This data can be written to file or be send over http
    """  
    if input_data=='test':
        with assets.get_exercise_test_data() as f:
            input_data=json.load(f)

    additional_params=[
        'Этап подготовки',
        'Часть тренировки',
        'Тип упражнения',
        'Продолжительность',
        'Количество игроков',
        'Организация',
        'Пространство',
        'Дозировка',
        'Пульс',
        'Касание мяча',
        'Нейтральные',
        'Расположение тренера',
        'Выявление победителя'
    ]

    render_options=RenderOptions(render_options)
    renderer=CompactRenderer(render_options=render_options)

    renderer.add_exercise_slide(exercise_data=input_data,additional_params=additional_params)
    renderer.save(to=output_file)