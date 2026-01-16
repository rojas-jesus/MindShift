<template>
  <div class="dashboard-container">
    <!-- Top Navigation Bar -->
    <header class="top-navigation">
      <div class="container-fluid">
        <div class="row align-items-center">
          <!-- Logo and Brand -->
          <div class="col-md-3">
            <div class="d-flex align-items-center">
              <h4 class="text-white mb-0 me-4">MindShift</h4>
            </div>
          </div>
          
          <!-- Navigation Links -->
          <div class="col-md-6">
            <nav class="nav justify-content-center">
              <RouterLink class="nav-link active" to="/smart-home">
                <i class="fas fa-brain me-2"></i>Mind
              </RouterLink>
              <RouterLink class="nav-link" to="/smart-home">
                <i class="fas fa-heart me-2"></i>Emotions
              </RouterLink>
              <RouterLink class="nav-link" to="/smart-home">
                <i class="fas fa-spa me-2"></i>Mindfulness
              </RouterLink>
              <RouterLink class="nav-link" to="/smart-home">
                <i class="fas fa-book me-2"></i>Journal
              </RouterLink>
              <RouterLink class="nav-link" to="/smart-home">
                <i class="fas fa-users me-2"></i>Support
              </RouterLink>
              <RouterLink class="nav-link" to="/smart-home">
                <i class="fas fa-chart-line me-2"></i>Progress
              </RouterLink>
              <RouterLink class="nav-link" to="/">
                <i class="fas fa-sign-out-alt me-2"></i>Logout
              </RouterLink>
            </nav>
          </div>
          
          <!-- User Actions -->
          <div class="col-md-3 text-end">
            <div class="d-inline-flex align-items-center">
              <div class="input-group me-3" style="max-width: 200px;">
                <span class="input-group-text bg-white border-end-0">
                  <i class="fas fa-search text-muted"></i>
                </span>
                <input type="text" class="form-control search-bar border-start-0" placeholder="Search...">
              </div>
              <span class="me-3 text-white">Scarlett</span>
              <div class="dropdown">
                <button class="btn btn-white dropdown-toggle" type="button" data-bs-toggle="dropdown">
                  <i class="fas fa-user-circle fa-lg"></i>
                </button>
              </div>
              <button class="btn btn-white ms-2">
                <i class="fas fa-bell fa-lg"></i>
              </button>
              <button class="btn btn-white ms-2">
                <i class="fas fa-cog fa-lg"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content-full">
      <div class="container-fluid p-4">
        <!-- Welcome Section -->
        <div class="row mb-4">
          <div class="col-12">
            <div class="card dashboard-card welcome-card p-4">
              <div class="row align-items-center">
                <div class="col-md-8">
                  <h2 class="mb-3">Hello, Scarlett!</h2>
                  <p class="mb-2">Welcome to your mind wellness dashboard</p>
                  <div class="d-flex align-items-center">
                    <i class="fas fa-brain me-2"></i>
                    <span class="me-3">Current Mood: {{ currentMood.level }}</span>
                    <span class="fs-4">{{ currentMood.emoji }}</span>
                  </div>
                </div>
                <div class="col-md-4 text-end">
                  <div class="text-center p-4 bg-white bg-opacity-25 rounded-3">
                    <i class="fas fa-brain fa-3x text-white mb-2"></i>
                    <p class="mb-0 text-white">Mind Wellness</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Main Thoughts Section -->
        <div class="row mb-4">
          <div class="col-12">
            <h4 class="mb-3">Daily Thoughts</h4>
            <div class="row">
              <div class="col-md-3 mb-3" v-for="thought in thoughts" :key="thought.id">
                <div class="card dashboard-card device-card" :class="{ active: thought.status }">
                  <div class="card-body text-center">
                    <i :class="`fas ${thought.icon} fa-2x mb-3`"></i>
                    <h6 class="card-title">{{ thought.name }}</h6>
                    <div class="form-check form-switch">
                      <input class="form-check-input" type="checkbox" :checked="thought.status" @change="toggleThought(thought.id)">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Secondary Row -->
        <div class="row mb-4">
          <!-- Inspirational Quote -->
          <div class="col-md-4">
            <InspirationalQuote />
          </div>

          <!-- Mind Tools -->
          <div class="col-md-4">
            <div class="card dashboard-card">
              <div class="card-body">
                <h5 class="card-title mb-3">Mind Tools</h5>
                <div class="mind-tool-item mb-3" v-for="tool in mindTools" :key="tool.id">
                  <div class="d-flex justify-content-between align-items-center p-2 rounded" :class="`device-${tool.color}`">
                    <div class="d-flex align-items-center">
                      <i :class="`fas ${tool.icon} me-2`"></i>
                      <span>{{ tool.name }}</span>
                    </div>
                    <div class="form-check form-switch">
                      <input class="form-check-input" type="checkbox" :checked="tool.status" @change="toggleMindTool(tool.id)">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Support Network -->
          <div class="col-md-4">
            <div class="card dashboard-card">
              <div class="card-body">
                <h5 class="card-title mb-3">Support Network</h5>
                <div class="member-item mb-3" v-for="member in members" :key="member.id">
                  <div class="d-flex align-items-center">
                    <div class="member-avatar me-3" :class="getAvatarColor(member.id)">
                      {{ member.avatar }}
                    </div>
                    <div>
                      <div class="fw-bold">{{ member.name }}</div>
                      <small class="text-muted">{{ member.role }}</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Emotional Temperature -->
        <div class="row mb-4">
          <div class="col-md-4">
            <div class="card dashboard-card">
              <div class="card-body text-center">
                <h5 class="card-title mb-3">Emotional State</h5>
                <div class="emotion-gauge mx-auto mb-3">
                  <div class="emotion-emoji">{{ currentMood.emoji }}</div>
                </div>
                <div class="emotion-label mb-3">{{ currentMood.level }}</div>
                <div class="d-flex justify-content-center align-items-center mb-3">
                  <button class="btn btn-outline-secondary btn-sm me-2" @click="decreaseEmotion">
                    <i class="fas fa-minus"></i>
                  </button>
                  <button class="btn btn-outline-secondary btn-sm" @click="increaseEmotion">
                    <i class="fas fa-plus"></i>
                  </button>
                </div>
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" checked>
                  <label class="form-check-label">Track Daily Mood</label>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mood History Chart -->
        <div class="row">
          <div class="col-12">
            <div class="card dashboard-card">
              <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-3">
                  <h5 class="card-title mb-0">Weekly Mood Journey</h5>
                  <span class="badge bg-info text-dark">Mindfulness Active</span>
                </div>
                <div class="mood-chart-container">
                  <canvas ref="moodChartCanvas"></canvas>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'
import { RouterLink } from 'vue-router'
import { useDashboardStore } from '../stores/dashboard'
import Chart from 'chart.js/auto'
import InspirationalQuote from '../components/InspirationalQuote.vue'

const dashboardStore = useDashboardStore()
const moodChartCanvas = ref<HTMLCanvasElement>()

const { thoughts, mindTools, members, emotionalTemperature, currentMood, moodHistory } = dashboardStore
const { toggleThought, toggleMindTool, setEmotionalTemperature } = dashboardStore

const increaseEmotion = () => {
  if (emotionalTemperature.value < 50) {
    setEmotionalTemperature(emotionalTemperature.value + 5)
  }
}

const decreaseEmotion = () => {
  if (emotionalTemperature.value > 0) {
    setEmotionalTemperature(emotionalTemperature.value - 5)
  }
}

const getAvatarColor = (id: number) => {
  const colors = ['purple', 'pink', 'blue', 'green', 'orange']
  return colors[id - 1] || 'purple'
}

const getMoodColor = (mood: number) => {
  if (mood < 15) return '#3B82F6'      // Blue - Sad
  if (mood < 25) return '#F59E0B'      // Orange - Anxious  
  if (mood < 35) return '#EAB308'      // Yellow - Balanced
  return '#10B981'                      // Green - Happy
}

onMounted(async () => {
  await nextTick()
  if (moodChartCanvas.value) {
    const ctx = moodChartCanvas.value.getContext('2d')
    if (ctx) {
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: moodHistory.value.map(m => m.day),
          datasets: [{
            label: 'Mood Level',
            data: moodHistory.value.map(m => m.mood),
            borderColor: '#8B5CF6',
            backgroundColor: 'rgba(139, 92, 246, 0.1)',
            borderWidth: 3,
            fill: true,
            tension: 0.4,
            pointBackgroundColor: moodHistory.value.map(m => getMoodColor(m.mood)),
            pointBorderColor: moodHistory.value.map(m => getMoodColor(m.mood)),
            pointRadius: 8,
            pointHoverRadius: 10
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: function(context) {
                  const moodData = moodHistory.value[context.dataIndex]
                  return `${moodData.emotion}: ${moodData.mood}`
                }
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              max: 50,
              title: {
                display: true,
                text: 'Mood Level'
              },
              grid: {
                color: 'rgba(0, 0, 0, 0.05)'
              }
            },
            x: {
              grid: {
                display: false
              }
            }
          }
        }
      })
    }
  }
})
</script>

<style scoped>
@import '../assets/dashboard.css';
</style>
