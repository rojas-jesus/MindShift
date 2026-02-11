<template>
  <div class="dashboard-layout">
    <!-- Top Navigation Bar -->


    <!-- Main Content -->
    <main class="main-content">
      <div class="container-fluid p-4">
        <!-- Welcome Section -->
        <div class="row mb-4">
          <div class="col-12">
            <div class="welcome-section">
              <h2>Hello, {{ userProfile?.username || userProfile?.first_name || 'User' }}!</h2>
              <p>Welcome to your mind wellness dashboard</p>
              <div class="mood-indicator">
                <HugeiconsIcon :icon="BrainIcon" class="me-2" />
                <span>Current Mood: Balanced</span>
                <span class="fs-4">😊</span>

              </div>
            </div>
          </div>
        </div>

        <!-- PUT ANY TEXT HERE -->
        <div class="row mb-2">
          <div class="col-12 px-4 mb-2">
            <span class="text-muted small fw-bold">PUT ANY TEXT HERE</span>
          </div>
        </div>

        <!-- Row 1: Raw Entry Actions -->
        <div class="row mb-3">
          <div class="col-12">
            <div class="action-row-card p-3">
              <div class="d-flex gap-3 align-items-center">
                <div class="custom-tooltip-container">
                  <RouterLink 
                    to="/thought-raw/create" 
                    class="btn btn-primary d-flex align-items-center"
                  >
                    <HugeiconsIcon :icon="Add01Icon" class="me-2" />
                    Raw Thought
                  </RouterLink>
                  <span class="tooltip-text">Speak freely and save your thought(s).</span>
                </div>

                <div class="custom-tooltip-container">
                  <RouterLink 
                    to="/action-raw/create" 
                    class="btn btn-outline-primary d-flex align-items-center"
                  >
                    <HugeiconsIcon :icon="Add01Icon" class="me-2" />
                    Raw Action
                  </RouterLink>
                  <span class="tooltip-text">Track your activities instantly.</span>
                </div>

                <div class="custom-tooltip-container">
                   <HugeiconsIcon :icon="InformationCircleIcon" size="20" class="text-muted" style="cursor: help;" />
                   <span class="tooltip-text">"Raw" entries allow for fast recording.</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Row 2: Utility Tools (Right Aligned) -->
        <div class="row mb-4">
          <div class="col-12">
            <div class="utility-row-card p-4">
              <div class="row">
                <div class="col-md-6 offset-md-6">
                  <div class="quick-btn-grid">
                    <button class="quick-btn purple long">
                      <HugeiconsIcon :icon="Sun01Icon" size="20" class="mb-1" />
                      <span>Morning Reflection</span>
                    </button>
                    <button class="quick-btn purple-light long">
                      <HugeiconsIcon :icon="FavouriteIcon" size="20" class="mb-1" />
                      <span>Gratitude</span>
                    </button>
                    <button class="quick-btn white long">
                      <HugeiconsIcon :icon="BrainIcon" size="20" class="mb-1" />
                      <span>Mental Health</span>
                    </button>
                    <button class="quick-btn purple long">
                      <HugeiconsIcon :icon="FastWindIcon" size="20" class="mb-1" />
                      <span>Focus</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Secondary Row -->
        <div class="row mb-4">
          <!-- Daily Inspiration -->
          <div class="col-md-4">
            <div class="inspiration-card">
              <h5 class="card-title mb-3">Daily Inspiration</h5>
              <div class="quote-content">
                <p class="quote-text">"The only way to do great work is to love what you do."</p>
                <p class="quote-author">- Steve Jobs</p>
              </div>
            </div>
          </div>

          <!-- Mind Tools -->
          <div class="col-md-4">
            <div class="tools-card">
              <h5 class="card-title mb-3">Mind Tools</h5>
              <div class="tool-item mb-3" v-for="tool in mindTools" :key="tool.id">
                <div class="d-flex justify-content-between align-items-center p-2 rounded tool-bg">
                  <div class="d-flex align-items-center">
                    <HugeiconsIcon :icon="getIcon(tool.icon)" class="me-2" />
                    <span>{{ tool.name }}</span>

                  </div>
                  <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" :checked="tool.status" @change="toggleMindTool(tool.id)">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Support -->
          <div class="col-md-4">
            <div class="support-card">
              <h5 class="card-title mb-3">Support</h5>
              <div class="support-item mb-3" v-for="member in members" :key="member.id">
                <div class="d-flex align-items-center">
                  <div class="support-avatar me-3" :class="getAvatarColor(member.id)">
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

        <!-- Mood Tracker -->
        <div class="row mb-4">
          <div class="col-md-4">
            <div class="mood-card">
              <h5 class="card-title mb-3">Mood Tracker</h5>
              <div class="emotion-gauge mx-auto mb-3">
                <div class="emotion-emoji">{{ currentMood.emoji }}</div>
              </div>
              <div class="emotion-label mb-3">{{ currentMood.level }}</div>
              <div class="d-flex justify-content-center align-items-center mb-3">
                <button class="btn btn-outline-secondary btn-sm me-2" @click="decreaseEmotion">
                  <HugeiconsIcon :icon="Remove01Icon" size="16" />
                </button>
                <button class="btn btn-outline-secondary btn-sm" @click="increaseEmotion">
                  <HugeiconsIcon :icon="Add01Icon" size="16" />
                </button>


              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useDashboardStore } from '../stores/dashboard'
import { authService } from '../services/auth'
import { 
  HugeiconsIcon 
} from '@hugeicons/vue'
import { 
  UserCircleIcon, 
  BrainIcon, 
  Add01Icon, 
  Remove01Icon,
  InformationCircleIcon,
  Sun01Icon,
  FavouriteIcon,
  SmileIcon,
  NaturalFoodIcon,
  FastWindIcon,
  StarIcon,
  ZzzIcon
} from '@hugeicons/core-free-icons'




const dashboardStore = useDashboardStore()
const { thoughts, mindTools, members, currentMood } = dashboardStore
const { toggleThought, toggleMindTool, setEmotionalTemperature } = dashboardStore

const userProfile = ref<any>(authService.getStoredUser())

onMounted(async () => {
  try {
    const response = await authService.getCurrentUser()
    userProfile.value = response.data
    localStorage.setItem('user_info', JSON.stringify(response.data))
  } catch (error) {
    console.error('Error fetching user profile:', error)
  }
})

const iconMap: Record<string, any> = {
  Sun01Icon,
  FavouriteIcon,
  SmileIcon,
  NaturalFoodIcon,
  FastWindIcon,
  StarIcon,
  BrainIcon,
  ZzzIcon
}


const getIcon = (name: string) => {
  return iconMap[name] || BrainIcon
}

const increaseEmotion = () => {
  if (dashboardStore.emotionalTemperature < 50) {
    setEmotionalTemperature(dashboardStore.emotionalTemperature + 5)
  }
}

const decreaseEmotion = () => {
  if (dashboardStore.emotionalTemperature > 0) {
    setEmotionalTemperature(dashboardStore.emotionalTemperature - 5)
  }
}

const getAvatarColor = (id: number) => {
  const colors = ['purple', 'pink', 'blue', 'green', 'orange']
  return colors[id - 1] || 'purple'
}
</script>

<style scoped>
.dashboard-layout {
  min-height: 100vh;
  background-color: #f8f9fa;
}



.main-content {
  background-color: #f8f9fa;
  min-height: calc(100vh - 80px);
}

.welcome-section {
  background: linear-gradient(135deg, #8B5CF6, #EC4899);
  color: white;
  padding: 2rem;
  border-radius: 20px;
  margin-bottom: 2rem;
}

.mood-indicator {
  display: flex;
  align-items: center;
  margin-top: 1rem;
}

.thought-card {
  border-radius: 20px;
  padding: 20px;
  margin-bottom: 15px;
  transition: all 0.3s ease;
  background: white;
  box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.thought-card:hover {
  transform: scale(1.02);
}

.thought-card.active {
  background-color: #8A2BE2;
  color: white;
}

.inspiration-card,
.tools-card,
.support-card,
.mood-card {
  border-radius: 20px;
  padding: 20px;
  background: white;
  box-shadow: 0 5px 20px rgba(0,0,0,0.08);
  height: 100%;
}

.quote-content {
  text-align: center;
  padding: 1rem;
}

.quote-text {
  font-style: italic;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.quote-author {
  font-weight: bold;
  color: #6A0DAD;
}

.tool-bg {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(236, 72, 153, 0.1));
}

.support-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: white;
  font-size: 1rem;
  box-shadow: 0 3px 10px rgba(0,0,0,0.2);
}

.emotion-gauge {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: conic-gradient(
    from 180deg,
    #3B82F6 0deg,    /* Blue for sad */
    #3B82F6 90deg,
    #F59E0B 90deg,    /* Orange for anxious */
    #F59E0B 180deg,
    #EAB308 180deg,   /* Yellow for balanced */
    #EAB308 270deg,
    #10B981 270deg,   /* Green for happy */
    #10B981 360deg
  );
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.emotion-gauge::before {
  content: '';
  position: absolute;
  width: 120px;
  height: 120px;
  background: white;
  border-radius: 50%;
}

.emotion-emoji {
  position: relative;
  z-index: 1;
  font-size: 2.5rem;
}

.emotion-label {
  text-align: center;
  font-weight: 600;
  color: #2C3E50;
}

/* Avatar colors */
.support-avatar.purple { background: #8B5CF6; }
.support-avatar.pink { background: #EC4899; }
.support-avatar.blue { background: #3B82F6; }
.support-avatar.green { background: #10B981; }
.support-avatar.orange { background: #F59E0B; }

/* Custom Tooltip Styles */
.custom-tooltip-container {
  position: relative;
  display: inline-block;
}

.tooltip-text {
  visibility: hidden;
  width: 220px;
  background-color: #333;
  color: #fff;
  text-align: center;
  border-radius: 8px;
  padding: 8px 12px;
  position: absolute;
  z-index: 100;
  bottom: 125%; /* Position above the button */
  left: 50%;
  margin-left: -110px;
  opacity: 0;
  transition: opacity 0.3s, transform 0.3s;
  transform: translateY(10px);
  font-size: 0.85rem;
  line-height: 1.4;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  pointer-events: none;
}

.tooltip-text::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #333 transparent transparent transparent;
}

.custom-tooltip-container:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
  transform: translateY(0);
}

/* Panel Cards */
.action-row-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
}

.utility-row-card {
  background: #fdfdfd;
  border-radius: 20px;
  border: 1px solid #f1f1f1;
  box-shadow: 0 5px 20px rgba(0,0,0,0.02);
}

.quick-btn-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.quick-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 15px;
  border-radius: 12px;
  border: none;
  font-size: 0.7rem;
  font-weight: 600;
  transition: all 0.2s ease;
  min-height: 65px;
}

.quick-btn.long {
  padding-left: 30px;
  padding-right: 30px;
}

.quick-btn:hover {
  transform: scale(1.02);
  filter: brightness(0.95);
}

.quick-btn.purple {
  background-color: #8B5CF6;
  color: white;
}

.quick-btn.purple-light {
  background-color: #A78BFA;
  color: white;
}

.quick-btn.white {
  background-color: #f6f8fa;
  color: #6a6a6a;
  border: 1px solid #eaedf0;
}

.quick-btn span {
  text-align: center;
  margin-top: 4px;
}
</style>
