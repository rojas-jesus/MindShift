<template>
  <div class="thoughts-view">
    <div class="container-fluid p-4">
      <!-- Header -->
      <div class="row mb-4">
        <div class="col-12">
          <h2 class="page-title">
            <HugeiconsIcon :icon="BrainIcon" class="me-3" size="32" />
            Thoughts Overview
          </h2>
          <p class="text-muted">Track and manage your mental wellness journey</p>
        </div>
      </div>

      <!-- Statistics Cards -->
      <div class="row mb-4">
        <div class="col-md-4 mb-3">
          <div class="stat-card">
            <div class="stat-icon purple">
              <HugeiconsIcon :icon="Note01Icon" size="28" />
            </div>
            <div class="stat-content">
              <h3 class="stat-number">{{ totalThoughts }}</h3>
              <p class="stat-label">Total Raw Thoughts</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-3">
          <div class="stat-card">
            <div class="stat-icon blue">
              <HugeiconsIcon :icon="BrainIcon" size="28" />
            </div>
            <div class="stat-content">
              <h3 class="stat-number">{{ thisWeekThoughts }}</h3>
              <p class="stat-label">This Week</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-3">
          <div class="stat-card">
            <div class="stat-icon green">
              <HugeiconsIcon :icon="Note01Icon" size="28" />
            </div>
            <div class="stat-content">
              <h3 class="stat-number">{{ thisMonthThoughts }}</h3>
              <p class="stat-label">This Month</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div class="row mb-4">
        <div class="col-12">
          <div class="actions-panel p-4">
            <h5 class="mb-3">Quick Actions</h5>
            <div class="d-flex gap-3 flex-wrap">
              <RouterLink to="/thought-raw/create" class="btn btn-primary btn-lg">
                <HugeiconsIcon :icon="Add01Icon" class="me-2" />
                Create Raw Thought
              </RouterLink>
              <RouterLink to="/thought-raw/list" class="btn btn-outline-primary btn-lg">
                <HugeiconsIcon :icon="Note01Icon" class="me-2" />
                View All Raw Thoughts
              </RouterLink>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Thoughts Preview -->
      <div class="row">
        <div class="col-12">
          <div class="recent-panel p-4">
            <div class="d-flex justify-content-between align-items-center mb-3">
              <h5 class="mb-0">Recent Thoughts</h5>
              <RouterLink to="/thought-raw/list" class="text-decoration-none">
                View All →
              </RouterLink>
            </div>
            
            <div v-if="loading" class="text-center py-5">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>

            <div v-else-if="recentThoughts.length === 0" class="text-center py-5 text-muted">
              <HugeiconsIcon :icon="Note01Icon" size="48" class="mb-3 opacity-50" />
              <p>No thoughts recorded yet. Start by creating your first raw thought!</p>
            </div>

            <div v-else class="thoughts-list">
              <div 
                v-for="thought in recentThoughts" 
                :key="thought.id"
                class="thought-item"
              >
                <div class="thought-content">
                  <p class="thought-text">{{ thought.transcription }}</p>
                  <small class="thought-time text-muted">
                    {{ formatDate(thought.timestamp) }}
                  </small>
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
import { ref, onMounted, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { HugeiconsIcon } from '@hugeicons/vue'
import { 
  BrainIcon,
  Note01Icon,
  Add01Icon
} from '@hugeicons/core-free-icons'
import { thoughtRawService, type ThoughtRawEntry } from '../services/thoughtRaw'

const thoughts = ref<ThoughtRawEntry[]>([])
const loading = ref(true)
const error = ref('')

const totalThoughts = computed(() => thoughts.value.length)

const thisWeekThoughts = computed(() => {
  const oneWeekAgo = new Date()
  oneWeekAgo.setDate(oneWeekAgo.getDate() - 7)
  return thoughts.value.filter(t => new Date(t.timestamp) >= oneWeekAgo).length
})

const thisMonthThoughts = computed(() => {
  const oneMonthAgo = new Date()
  oneMonthAgo.setMonth(oneMonthAgo.getMonth() - 1)
  return thoughts.value.filter(t => new Date(t.timestamp) >= oneMonthAgo).length
})

const recentThoughts = computed(() => {
  return thoughts.value.slice(0, 5)
})

const formatDate = (timestamp: string) => {
  const date = new Date(timestamp)
  const now = new Date()
  const diffMs = now.getTime() - date.getTime()
  const diffMins = Math.floor(diffMs / 60000)
  const diffHours = Math.floor(diffMs / 3600000)
  const diffDays = Math.floor(diffMs / 86400000)

  if (diffMins < 1) return 'Just now'
  if (diffMins < 60) return `${diffMins} min${diffMins > 1 ? 's' : ''} ago`
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`
  if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`
  
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

onMounted(async () => {
  try {
    thoughts.value = await thoughtRawService.getAllThoughtRaw()
    // Sort by timestamp descending (newest first)
    thoughts.value.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime())
  } catch (err: any) {
    console.error('Failed to load thoughts:', err)
    error.value = err.message || 'Failed to load thoughts'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.thoughts-view {
  min-height: calc(100vh - 80px);
  background-color: #f8fafc;
}

.page-title {
  display: flex;
  align-items: center;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.stat-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  transition: transform 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.stat-icon.purple {
  background: linear-gradient(135deg, #8B5CF6, #A78BFA);
}

.stat-icon.blue {
  background: linear-gradient(135deg, #3B82F6, #60A5FA);
}

.stat-icon.green {
  background: linear-gradient(135deg, #10B981, #34D399);
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.25rem;
}

.stat-label {
  color: #6b7280;
  margin: 0;
  font-size: 0.9rem;
}

.actions-panel,
.recent-panel {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.actions-panel h5,
.recent-panel h5 {
  color: #1a202c;
  font-weight: 600;
}

.thoughts-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.thought-item {
  padding: 16px;
  background: #f8fafc;
  border-radius: 12px;
  border-left: 4px solid #8B5CF6;
  transition: all 0.2s ease;
}

.thought-item:hover {
  background: #f1f5f9;
  transform: translateX(4px);
}

.thought-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.thought-text {
  margin: 0;
  color: #1a202c;
  font-size: 0.95rem;
  line-height: 1.5;
}

.thought-time {
  font-size: 0.8rem;
}

.btn-lg {
  padding: 12px 24px;
  font-weight: 600;
  border-radius: 12px;
}
</style>
