<template>
  <div class="action-create-view">
    <div class="container mt-4">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <div class="card shadow">
            <div class="card-header bg-primary text-white">
              <h4 class="mb-0">
                <HugeiconsIcon :icon="BrainIcon" class="me-2" />
                Create New Action
              </h4>
            </div>
            <div class="card-body">
              <!-- Tabs Navigation -->
              <ul class="nav nav-tabs mb-4" role="tablist">
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link"
                    :class="{ active: activeTab === 'voice' }"
                    @click="activeTab = 'voice'"
                    type="button"
                  >
                    <HugeiconsIcon :icon="Mic01Icon" class="me-2" />
                    Voice Input
                  </button>
                </li>
                <li class="nav-item" role="presentation">
                  <button
                    class="nav-link"
                    :class="{ active: activeTab === 'manual' }"
                    @click="activeTab = 'manual'"
                    type="button"
                  >
                    <HugeiconsIcon :icon="PencilEdit01Icon" class="me-2" />
                    Manual Form
                  </button>
                </li>
              </ul>

              <!-- Tab Content -->
              <div class="tab-content">
                <!-- Voice Input Tab -->
                <div v-if="activeTab === 'voice'" class="tab-pane fade show active">
                  <VoiceActionInput />
                </div>

                <!-- Manual Form Tab -->
                <div v-if="activeTab === 'manual'" class="tab-pane fade show active">
                  <div class="alert alert-info d-flex align-items-center">
                    <HugeiconsIcon :icon="InformationCircleIcon" class="me-2" />
                    Use the manual form to create structured action entries with all fields.
                    For a quick voice entry, switch to the Voice Input tab.
                  </div>
                  <p class="text-muted">
                    Manual form functionality will be implemented here.
                    This allows you to fill in all action details including name, description,
                    advantages, disadvantages, emotion, and duration.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import VoiceActionInput from '../components/VoiceActionInput.vue';
import { HugeiconsIcon } from '@hugeicons/vue';
import {
  BrainIcon,
  Mic01Icon,
  PencilEdit01Icon,
  InformationCircleIcon
} from '@hugeicons/core-free-icons';

const activeTab = ref<'voice' | 'manual'>('voice');
</script>

<style scoped>
.action-create-view {
  min-height: calc(100vh - 100px);
  background-color: #f8f9fa;
  padding: 2rem 0;
}

.nav-tabs {
  border-bottom: 2px solid #dee2e6;
}

.nav-tabs .nav-link {
  color: #6c757d;
  border: none;
  border-bottom: 3px solid transparent;
  padding: 12px 24px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.nav-tabs .nav-link:hover {
  border-bottom-color: #6c757d;
  color: #495057;
}

.nav-tabs .nav-link.active {
  color: #0d6efd;
  border-bottom-color: #0d6efd;
  background-color: transparent;
}

.card {
  border: none;
  border-radius: 15px;
}

.card-header {
  border-radius: 15px 15px 0 0 !important;
  padding: 1.5rem;
}

.tab-content {
  padding: 1rem 0;
}
</style>


