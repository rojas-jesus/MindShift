<template>
  <div class="thought-create-view">
    <div class="container mt-4">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <div class="card shadow">
            <div class="card-header bg-primary text-white">
              <h4 class="mb-0">
                <HugeiconsIcon :icon="BrainIcon" class="me-2" />
                Create New Thought
              </h4>
            </div>
            <div class="card-body">
              <div class="thought-input-container">
                <ThoughtRawInput />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import ThoughtRawInput from '../components/ThoughtRawInput.vue';
import { HugeiconsIcon } from '@hugeicons/vue';
import { BrainIcon } from '@hugeicons/core-free-icons';
</script>

<style scoped>
.thought-create-view {
  min-height: calc(100vh - 100px);
  background-color: #f8f9fa;
  padding: 2rem 0;
}

.card {
  border: none;
  border-radius: 15px;
  overflow: hidden;
}

.card-header {
  padding: 1.5rem;
}

.card-body {
  padding: 2rem;
}
</style>
