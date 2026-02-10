import api from './auth';

export interface VoiceActionEntry {
  id: number;
  transcription: string;
  timestamp: string;
}

export const voiceActionService = {
  async createVoiceAction(transcription: string): Promise<VoiceActionEntry> {
    console.log('VOICE_ACTION_TRACE: Attempting to save action to api/voice/action/create/');
    try {
      const response = await api.post('api/voice/action/create/', {
        transcription,
      });
      console.log('VOICE_ACTION_TRACE: Success!', response.status);
      return response.data;
    } catch (error: any) {
      console.error('VOICE_ACTION_TRACE: Failed!', error.response?.status, error.message);
      throw error;
    }
  },
};
