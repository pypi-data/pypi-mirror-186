from nf_presentation.renderers.base_renderer import BaseRenderer
from nf_presentation.data_classes import SingleExerciseInfo
from nf_presentation.builders import ParagraphBuilder

from nf_presentation._settings import compact_layout as current_layout
import nf_presentation.settings as base_settings
from nf_presentation.logger import logger

_default_description="""Описание:



Тренерские акценты:


"""

class RenderOptions:
    _media_fields=['video_1','video_2','animation_1','animation_2']
    _scheme_priority=['scheme_1','scheme_2']
    def __init__(self,raw_data:dict):
        self.raw_data:dict=raw_data
        self.check()
    @property
    def media_fields_to_render(self) -> list[str]:
        """returns a list of edia fields should be rendered to a pptx
        ['video_2','animation_1']"""
        return [field for field in self._media_fields if self.raw_data.get(field)]  # if checked as True
    @property
    def schemes_to_render(self):
        return [scheme_name for scheme_name in self._scheme_priority if self.raw_data.get(scheme_name)]
    def check(self):
        #check if video or animation will be added to pptx
        if not any([self.raw_data.get(field) for field in self._media_fields]):
            logger.warn('(Render Options) no player links are marked to be added to pptx')
        if not any(self.schemes_to_render):
            logger.warn('(Render Options) no scheme links are marked to be added to pptx')






class CompactRenderer(BaseRenderer):
    def __init__(self, render_options:RenderOptions):
        super().__init__(ratio=base_settings.PRESENTATION_RATIO)
        self.render_options : RenderOptions = render_options
    def add_exercise_slide(self, exercise_data:dict,additional_params:list[str]=None):
        """
        Arguments:
            additional_params: if None- data would be taken from exercise info,
                if not - using current list of additional params"""
        exercise=SingleExerciseInfo(raw_data=exercise_data)
        slide=self.presentation_builder.create_slide()

        title=slide.create_title(base_settings.DEFAULT_SLIDE_TITLE).at(current_layout.TITLE_POSITION).with_size(current_layout.TITLE_SIZE)
        title.with_foreground(current_layout.TITLE_FOREGROUND).with_background(current_layout.TITLE_BACKGROUND)

        #decription_text=HTMLRenderer().render(exercise.description)
        description_text=_default_description
        right_table=slide.create_table().at(current_layout.RIGHT_TABLE_POSITION).with_width(current_layout.RIGHT_TABLE_WIDTH)
        right_table.append_row(description_text)
        # mayble here add default params iter
        
        if additional_params is None:
            left_rows=exercise.additional_params.items()
        else:
            left_rows=[(param,'') for param in additional_params]

        if current_layout.CAPITALIZE_ADDITIONAL_DATA:
            capitalized_rows=[]
            for row in left_rows:
                capitalized_rows.append((text.upper() for text in row))
            left_rows=capitalized_rows

        left_table=slide.create_table().at(current_layout.LEFT_TABLE_POSITION).with_width(current_layout.LEFT_TABLE_WIDTH)
        left_table.append_row(exercise.title)
        left_table.append_empty_row()
        
        for row in left_rows:
           left_table.append_row(*row) 

        #schemes
        scheme_added=False
           
        for scheme_name in self.render_options.schemes_to_render:
            scheme=exercise.get_scheme_by_name(scheme_name)
            if not scheme:
                logger.warn(f'Cant add scheme "{scheme}" to slide, because it is not in the exercise data')
                continue      

            image_stream=scheme.to_stream()
            if not image_stream:
                logger.warn(f'cant add scheme "{scheme}" to slide, because its stream is None')
                continue

            self._open_streams.append(image_stream)
            slide.create_image(image_stream).at(current_layout.SCHEME_POSITION).set_size(current_layout.SCHEME_WIDTH,None)

            scheme_added=True
            break
        if not scheme_added:
            logger.error('No scheme added to slide. ')
            #TODO image fallback

        #add links
        links_added=False
        links_table=slide.create_table().at(current_layout.LINKS_TABLE_POSITION).with_width(current_layout.LEFT_TABLE_WIDTH)
        
        pb=ParagraphBuilder()
        #link_position=current_layout.LINKS_AREA
        video_counter=0
        animation_counter=0
        for media_field in self.render_options.media_fields_to_render:
            media=exercise.get_media(media_field)
            if not media.exist:
                logger.error(f'requested "{media_field}" is not in the current exercise. skipping')
                continue


            player_url=exercise.get_media(media_field).nftv_player
            is_animation='animation' in media_field
            if is_animation:
                animation_counter=animation_counter+1
            else:
                video_counter=video_counter+1
            
            

            pb.append_link(
                link_text=f"Анимация {animation_counter}" if is_animation else f"Видео {video_counter}",
                href=player_url)
            pb.append_text(' ')

            

            #image_file=current_layout.LINKS_ANIMATION_ICON_FILENAME if is_animation else current_layout.LINKS_VIDEO_ICON_FILENAME
            #image_stream=assets.convert_to_png(filename=image_file)
            #self.track_stream(image_stream)
            #slide.create_image(image_file=image_stream).at(link_position).with_size(current_layout.LINKS_IMAGE_SIZE).with_href(player_url)

            #x_delta,_=current_layout.LINKS_IMAGE_SIZE
            #x,y=link_position
            #link_position=(x+x_delta,y)

            links_added=True
        links_table.append_row('Ссылки',pb)

        if not links_added:
            logger.warn('No links added to presentation')



