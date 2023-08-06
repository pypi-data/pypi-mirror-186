# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from os.path import join, dirname, isfile, expanduser
from pathlib import Path
from typing import Optional, Union
from neon_utils.parse_utils import clean_quotes, clean_filename
from ovos_utils.log import LOG
from ovos_plugin_manager.templates.tts import TTS, TTSValidator
from ovos_config.locations import get_xdg_data_save_path
from ovos_workshop.resource_files import ResourceType, ResourceFile


class AudioFileTTS(TTS):
    def __init__(self, lang="en-us", config=None):
        super(AudioFileTTS, self).__init__(lang, config,
                                           AudioFileTTSValidator(self),
                                           audio_ext="wav",
                                           ssml_tags=[])
        self.res_type = ResourceType('audio_file', f'.{self.audio_ext}')
        self.res_type.user_directory = expanduser(
            self.config.get('audio_file_path')) or \
            join(get_xdg_data_save_path(), "AudioFileTTS")
        self.res_type.base_directory = join(dirname(__file__), 'audio')

    def _resolve_audio_file(self, file_basename: str) -> \
            Union[Path, str, None]:
        """
        Resolve the specified TTS audio file for the specified language
        Args:
            file_basename: filename to locate,
                           optionally with specified voice directory
        Returns:
            str or Path representation of the requested audio file else None
        """
        if '/' in file_basename:
            user_file = join(self.res_type.user_directory,
                             file_basename + self.res_type.file_extension)
            if isfile(user_file):
                return user_file
            base_file = join(self.res_type.base_directory,
                             file_basename + self.res_type.file_extension)
            if isfile(base_file):
                return base_file
        else:
            resource_file = ResourceFile(self.res_type, file_basename)
            return resource_file.file_path

    def get_tts(self, sentence: str, output_file: str,
                speaker: Optional[dict] = None):
        audio_file = self._resolve_audio_file(sentence)
        if not audio_file:
            sentence = clean_quotes(sentence)
            audio_file = self._resolve_audio_file(sentence)
        if not audio_file:
            sentence = clean_filename(sentence)
            audio_file = self._resolve_audio_file(sentence)
        if not audio_file:
            sentence = sentence.lower()
            audio_file = self._resolve_audio_file(sentence)
        # TODO: Fallback here with regex search
        audio_file = str(audio_file) if audio_file else None
        if not audio_file:
            LOG.error(f"No Audio File resolved for: '{sentence}' in paths: "
                      f"{self.res_type.user_directory}, "
                      f"{self.res_type.base_directory}")
        return audio_file, None


class AudioFileTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(AudioFileTTSValidator, self).__init__(tts)

    def validate_lang(self):
        # TODO: Add some validation of `self.lang` default language
        pass

    def validate_dependencies(self):
        # TODO: Optionally check dependencies or raise
        pass

    def validate_connection(self):
        # TODO: Optionally check connection to remote service or raise
        pass

    def get_tts_class(self):
        return AudioFileTTS
