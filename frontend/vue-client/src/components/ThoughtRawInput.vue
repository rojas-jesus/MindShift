<template>
  <div class="voice-thought-input">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title mb-3 d-flex align-items-center">
          <HugeiconsIcon :icon="Mic01Icon" class="me-2" />
          Voice Input
        </h5>


        <!-- Browser Support Check -->
        <div v-if="!isSupported" class="alert alert-warning d-flex align-items-center">
          <HugeiconsIcon :icon="Alert01Icon" class="me-2" />
          Your browser doesn't support voice recognition. Please use Chrome, Edge, or Safari.
        </div>


        <!-- Recording Controls -->
        <div v-if="isSupported" class="recording-section">
          <!-- Internet Connection Warning -->
          <!-- Info Alert -->
          <div class="alert alert-info mb-3 d-flex align-items-start text-start">
            <HugeiconsIcon :icon="InformationCircleIcon" class="me-2 mt-1" />
            <div>
              <strong>Note:</strong> If voice recognition isn't working, you can type your thoughts directly in the text area above.
              Also if you are in Windows 10/11, you can also use <strong>Windows button + H</strong>, so you can speak and it's gonna get transcribed.
            </div>
          </div>

          <div class="d-flex justify-content-center mb-3">
            <button
              v-if="!isRecording"
              @click="startRecording"
              class="btn btn-primary btn-lg d-flex align-items-center"
              :disabled="isSubmitting"
            >
              <HugeiconsIcon :icon="Mic01Icon" class="me-2" />
              Start Recording
            </button>

            <button
              v-else
              @click="stopRecording"
              class="btn btn-danger btn-lg d-flex align-items-center"
            >
              <HugeiconsIcon :icon="StopIcon" class="me-2" />
              Stop Recording
            </button>

          </div>

          <!-- Recording Indicator -->
          <div v-if="isRecording" class="recording-indicator text-center mb-3">
            <div class="pulse-animation">
              <HugeiconsIcon :icon="Mic01Icon" size="48" class="text-danger mx-auto" />
            </div>
            <p class="mt-2 text-muted">Listening... Speak now</p>
          </div>


          <!-- Transcription Display -->
          <div class="transcription-section mb-3">
            <label class="form-label">Transcription:</label>
            <textarea
              v-model="transcription"
              class="form-control"
              rows="5"
              placeholder="Your transcribed text will appear here, or you can type manually if voice recognition is not working..."
              :disabled="isRecording"
            ></textarea>
            <div v-if="interimText && !transcription" class="text-muted mt-2">
              <small><i>Listening: {{ interimText }}</i></small>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="action-buttons mb-3">
            <button
              v-if="!isRecording"
              @click="submitTranscription"
              class="btn btn-success d-inline-flex align-items-center"
              :disabled="isSubmitting || !transcription.trim()"
            >
              <span v-if="isSubmitting" class="spinner-border spinner-border-sm me-2"></span>
              <HugeiconsIcon v-else :icon="FloppyDiskIcon" class="me-2" />
              {{ isSubmitting ? 'Saving...' : 'Save Thought Entry' }}
            </button>

            <button
              v-if="transcription && !isRecording"
              @click="clearTranscription"
              class="btn btn-secondary d-inline-flex align-items-center"
              :disabled="isSubmitting"
            >
              <HugeiconsIcon :icon="RefreshIcon" class="me-2" />
              Clear
            </button>
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="alert alert-success mt-3 d-flex align-items-center">
            <HugeiconsIcon :icon="CheckmarkCircle01Icon" class="me-2" />
            {{ successMessage }}
          </div>


          <!-- Error Message -->
          <div v-if="errorMessage" class="alert alert-danger mt-3 d-flex align-items-center">
            <HugeiconsIcon :icon="AlertCircleIcon" class="me-2" />
            {{ errorMessage }}

            <div v-if="errorMessage.includes('Network') || errorMessage.includes('network')" class="mt-2">
              <button @click="retryRecording" class="btn btn-sm btn-outline-danger me-2 d-inline-flex align-items-center">
                <HugeiconsIcon :icon="RefreshIcon" size="14" class="me-1" />
                Retry
              </button>

              <small class="text-muted d-block mt-2">
                You can also type your thoughts manually in the text area above if voice recognition continues to fail.
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { thoughtRawService } from '../services/thoughtRaw';
import { HugeiconsIcon } from '@hugeicons/vue';
import {
  Mic01Icon,
  Alert01Icon,
  InformationCircleIcon,
  StopIcon,
  Idea01Icon,
  FloppyDiskIcon,
  RefreshIcon,
  CheckmarkCircle01Icon,
  AlertCircleIcon
} from '@hugeicons/core-free-icons';



const isSupported = ref(false);
const isRecording = ref(false);
const transcription = ref('');
const interimText = ref('');
const isSubmitting = ref(false);
const successMessage = ref('');
const errorMessage = ref('');

let recognition: any = null;

onMounted(() => {
  // Check for browser support
  const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
  
  if (SpeechRecognition) {
    isSupported.value = true;
    recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    recognition.onresult = (event: any) => {
      let finalTranscript = '';
      let interimTranscript = '';

      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += transcript + ' ';
        } else {
          interimTranscript += transcript;
        }
      }

      if (finalTranscript) {
        transcription.value += finalTranscript;
        interimText.value = '';
      } else {
        interimText.value = interimTranscript;
      }
    };

    recognition.onerror = (event: any) => {
      console.error('Speech recognition error:', event.error);
      isRecording.value = false;
      
      if (event.error === 'no-speech') {
        errorMessage.value = 'No speech detected. Please try again and speak clearly.';
      } else if (event.error === 'audio-capture') {
        errorMessage.value = 'No microphone found. Please check your microphone connection and try again.';
      } else if (event.error === 'not-allowed') {
        errorMessage.value = 'Microphone permission denied. Please allow microphone access in your browser settings and refresh the page.';
      } else if (event.error === 'network') {
        errorMessage.value = 'Network error: Unable to connect to speech recognition service. Please check your internet connection and try again. If the problem persists, you can type your thoughts manually in the text area below.';
      } else if (event.error === 'aborted') {
        errorMessage.value = 'Recording was aborted. Please try again.';
      } else if (event.error === 'bad-grammar') {
        errorMessage.value = 'Grammar error. Please try speaking again.';
      } else {
        errorMessage.value = `Recognition error: ${event.error}. Please check your internet connection and try again.`;
      }
    };

    recognition.onend = () => {
      isRecording.value = false;
    };
  }
});

onUnmounted(() => {
  if (recognition && isRecording.value) {
    recognition.stop();
  }
});

const startRecording = () => {
  if (!recognition) return;
  
  // Check if already recording
  if (isRecording.value) {
    return;
  }
  
  try {
    // Clear previous errors but keep transcription if user wants to edit
    errorMessage.value = '';
    successMessage.value = '';
    interimText.value = '';
    isRecording.value = true;
    recognition.start();
  } catch (error: any) {
    console.error('Error starting recognition:', error);
    if (error.message && error.message.includes('already started')) {
      // Recognition already running, just update state
      isRecording.value = true;
    } else {
      errorMessage.value = 'Failed to start recording. Please check your internet connection and try again.';
      isRecording.value = false;
    }
  }
};

const stopRecording = () => {
  if (recognition && isRecording.value) {
    recognition.stop();
    isRecording.value = false;
  }
};

const clearTranscription = () => {
  transcription.value = '';
  interimText.value = '';
  errorMessage.value = '';
  successMessage.value = '';
};

const retryRecording = () => {
  errorMessage.value = '';
  // Wait a moment before retrying
  setTimeout(() => {
    startRecording();
  }, 500);
};

const submitTranscription = async () => {
  if (!transcription.value.trim()) {
    errorMessage.value = 'Please record or enter some text before saving.';
    return;
  }

  isSubmitting.value = true;
  errorMessage.value = '';
  successMessage.value = '';

  try {
    await thoughtRawService.createThoughtRaw(transcription.value.trim());
    successMessage.value = 'Raw thought saved successfully!';
    transcription.value = '';
    interimText.value = '';
    
    // Clear success message after 3 seconds
    setTimeout(() => {
      successMessage.value = '';
    }, 3000);
  } catch (error: any) {
    console.error('Error saving raw thought:', error);
    errorMessage.value = error.response?.data?.detail || error.message || 'Failed to save raw thought. Please try again.';
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.voice-thought-input {
  max-width: 800px;
  margin: 0 auto;
}

.recording-indicator {
  padding: 20px;
}

.pulse-animation {
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.7;
    transform: scale(1.1);
  }
}

.transcription-section textarea {
  font-family: monospace;
  resize: vertical;
}

.action-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: none;
}

.card-title {
  color: #333;
  font-weight: 600;
}
</style>

