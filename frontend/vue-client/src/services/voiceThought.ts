import api from './auth';

export interface VoiceThoughtEntry {
  id: number;
  transcription: string;
  timestamp: string;
}

export const voiceThoughtService = {
  async createVoiceThought(transcription: string): Promise<VoiceThoughtEntry> {
    console.log('VOICE_THOUGHT_TRACE: Attempting to save thought to api/voice/thought/create/');
    try {
      const response = await api.post('api/voice/thought/create/', {
        transcription,
      });
      console.log('VOICE_THOUGHT_TRACE: Success!', response.status);
      return response.data;
    } catch (error: any) {
      console.error('VOICE_THOUGHT_TRACE: Failed!', error.response?.status, error.message);
      throw error;
    }
  },
};
