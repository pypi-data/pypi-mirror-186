from abc import abstractmethod
from typing import IO

from .settings import (
                    EMPY_DESCRIPLION_REPLACEMENT,
                    EMPTY_TRAINER_NAME_REPLACEMENT,
                    UNKNOWN_GROUP_ID_NAME_REPLACEMENT)

from ._settings.basic import create_player_link
from nf_presentation.scheme_renderer import SchemeRenderer, NewSchemeRenderer
from nf_presentation.logger import logger



class GroupInfo:
    """a class representing a position of exercise, in A1, A2, A3 B3 and others"""
    _group_names={
        1:'A',
        2:'B',
        3:'C'
    }
    def __init__(self, group_id:int, order:int):
        self._group_id=group_id
        self._order=order
    @property
    def id(self):
        return self._group_id
    @property
    def name(self):
        return self._group_names.get(self.id,UNKNOWN_GROUP_ID_NAME_REPLACEMENT)
    def __str__(self):
        return f'{self.name}{self._order}'

class AdditionalInfo:
    def __init__(self,data:dict):
        self.raw_data=data
    @property 
    def name(self):
        return self.raw_data.get('additional_name',{}).get('ru')
    @property
    def value(self):
        return self.raw_data.get('note')

class ExerciseInfo:
    def __init__(self, data:dict):
        self.raw_data : dict = data
        self._additionals : list[AdditionalInfo] = None
    @property
    def name(self):
        return self.raw_data.get('exercise_name',{}).get('ru')
    @property
    def scheme_main(self):
        return self.raw_data.get('exercise_scheme',{}).get('scheme_1')
    @property
    def description(self):
        description=self.raw_data.get('description')
        return description if description else EMPY_DESCRIPLION_REPLACEMENT
    @property
    def duration(self):
        return self.raw_data.get('duration')
    @property 
    def additionals(self) -> list[AdditionalInfo]:
        if self._additionals is None:
            # refactor!
            self._additionals=[AdditionalInfo(data) for data in self.raw_data.get('additional',[])]
            self._additionals.insert(0,AdditionalInfo({
                    "id": -1,
                    "additional_name": {
                        "en": "Duration",
                        "ru": "Длительность"
                    },
                    "training_exercise_id": -1,
                    "additional_id": -1,
                    "note": self.duration
                })) ##adding time
        return self._additionals
    @property
    def group(self) -> GroupInfo:
        return GroupInfo(
            group_id=self.raw_data.get('group'),
            order=self.raw_data.get('order'))



class TrainingInfo:
    def __init__(self,data:dict):
        self.raw_data=data
        self._exercises : list[ExerciseInfo] = None

    @property
    def exercises(self) -> list[ExerciseInfo]:
        if self._exercises is None:
            self._exercises= [ExerciseInfo(data) for data in self.raw_data.get('exercises_info')]
        return self._exercises

    @property
    def trainer_name(self):
        trainer_name =self.raw_data.get('trainer')
        return trainer_name if trainer_name else EMPTY_TRAINER_NAME_REPLACEMENT



# a class for exercise info of single exercise, it has a different scructure :(

class MediaLink:
    def __init__(self, raw_data):
        self.raw_data=raw_data
    @property
    def exist(self):
        return self.id!=-1
    @property
    def id(self):
        return self.raw_data.get('id')
    @property
    def nftv_id(self):
        return self.raw_data.get('links',{}).get('nftv')
    @property
    def youtube_id(self):
        return self.raw_data.get('links',{}).get('youtube')
    @property
    def nftv_player(self):
        return create_player_link(self.nftv_id)

class Scheme:
    @abstractmethod
    def to_stream(self)-> IO:
        pass

class OldScheme(Scheme):
    def __init__(self, svg_text:str):
        self.svg_text=svg_text
    def to_stream(self) -> IO:
        return SchemeRenderer().to_stream(self.svg_text)

class NewScheme(Scheme):
    def __init__(self, scheme_id):
        self.scheme_id=scheme_id
    def to_stream(self) -> IO:
        return NewSchemeRenderer().to_stream(self.scheme_id)

    

class SingleExerciseInfo:
    """A class representing info we get for an exercise to a python object"""
    _media_fields=['video_1','video_2','animation_1','animation_2']
    _sheme_fields=['scheme_1','scheme_2']

    def __init__(self, raw_data:dict):
        self.raw_data=raw_data
    @property
    def additional_params(self) -> dict:
        """returning exercise.additinal_params as dict, converting from list[dict]"""
        return { entry.get('title',''):entry.get('value','') for entry in self.raw_data.get('additional_params',{})}
    @property
    def description(self):
        return self.raw_data.get('description','')
    @property
    def title(self):
        return self.raw_data.get('title','')
    @property
    def old_schemes(self):
        return self.raw_data.get('scheme_data',[])
    @property
    def video_1(self):
         return MediaLink(self.raw_data.get('video_1'))
    @property
    def video_2(self):
         return MediaLink(self.raw_data.get('video_2'))
    @property
    def animation_1(self):
         return MediaLink(self.raw_data.get('animation_1'))
    @property
    def animation_2(self):
         return MediaLink(self.raw_data.get('animation_2'))
    def get_media(self, field_name):
        """returns a media link to videos
        Attributes:
            field_name:'video_1','video_2','animation_1',...
        
        Returns:
            a MediaLink object or None
            """
        if field_name not in self._media_fields:
            logger.warn(f'trying to get media field "{field_name}" from exercise_data, safe choices are {self._media_fields}')
        return MediaLink(self.raw_data.get(field_name))
    @property
    def medias(self):
        """returns a collection of medias like video1, video2 and others"""
    @property
    def media_as_dict(self):
        """returns a dict of existing(!) medias
            ex.
            {
                'video_1':MediaLink(...),
                'animation_1':MediaLink(...)"""
        return {field:self.raw_data.get(field) for field in self._media_fields}
    @property
    def scheme_1(self):
        scheme_id=self.raw_data.get('scheme_1')
        if scheme_id:
            return NewScheme(scheme_id=scheme_id)
        else:
            return OldScheme(svg_text=self.old_schemes[0])
    @property
    def scheme_2(self):
        scheme_id=self.raw_data.get('scheme_2')
        if scheme_id:
            return NewScheme(scheme_id=scheme_id)
        else:
            return OldScheme(svg_text=self.old_schemes[1])
    def get_scheme_by_name(self,name:str) -> Scheme:
        if name not in self._sheme_fields:
            logger.warn(f'attemping to get scheme with name "{name}", while allowed names are {self._sheme_fields}')
        #TODO add a fallback if scheme not found
        return getattr(self,name)

