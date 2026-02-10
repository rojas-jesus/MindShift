import api from './auth';

export interface ActionRawEntry {
  id: number;
  transcription: string;
  timestamp: string;
}

export const actionRawService = {
  async createActionRaw(transcription: string): Promise<ActionRawEntry> {
    console.log('ACTION_RAW_TRACE: Attempting to save action to api/action-raw/create/');
    try {
      const response = await api.post('api/action-raw/create/', {
        transcription,
      });
      console.log('ACTION_RAW_TRACE: Success!', response.status);
      return response.data;
    } catch (error: any) {
      console.error('ACTION_RAW_TRACE: Failed!', error.response?.status, error.message);
      throw error;
    }
  },
};
