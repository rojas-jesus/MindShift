<template>
  <div class="dashboard-layout">
    <!-- Top Navigation Bar -->
    <header class="top-nav">
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
              <RouterLink class="nav-link" to="/">Home</RouterLink>
              <RouterLink class="nav-link" to="/about">About</RouterLink>
              <RouterLink class="nav-link active" to="/smart-home">Dashboard</RouterLink>
              <RouterLink class="nav-link logout-btn" to="/">Logout</RouterLink>
            </nav>
          </div>
          
          <!-- User Actions -->
          <div class="col-md-3 text-end">
            <div class="d-inline-flex align-items-center">
              <span class="me-3 text-white">Scarlett</span>
              <div class="dropdown">
                <button class="btn btn-white dropdown-toggle" type="button" data-bs-toggle="dropdown">
                  <HugeiconsIcon :icon="UserCircleIcon" size="24" />

                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <div class="container-fluid p-4">
        <!-- Welcome Section -->
        <div class="row mb-4">
          <div class="col-12">
            <div class="welcome-section">
              <h2>Hello, Scarlett!</h2>
              <p>Welcome to your mind wellness dashboard</p>
              <div class="mood-indicator">
                <HugeiconsIcon :icon="BrainIcon" class="me-2" />
                <span>Current Mood: Balanced</span>
                <span class="fs-4">😊</span>

              </div>
            </div>
          </div>
        </div>

        <!-- Daily Thoughts Section -->
        <div class="row mb-4">
          <div class="col-12">
            <div class="d-flex justify-content-between align-items-center mb-3">
              <h4 class="mb-0">Daily Thoughts</h4>
              <RouterLink to="/thought/create" class="btn btn-primary">
                <HugeiconsIcon :icon="Add01Icon" class="me-2" />
                Add Thought

              </RouterLink>
            </div>
            <div class="row">
              <div class="col-md-3 mb-3" v-for="thought in thoughts" :key="thought.id">
                <div class="thought-card" :class="{ active: thought.status }">
                  <div class="card-body text-center">
                    <HugeiconsIcon :icon="getIcon(thought.icon)" size="32" class="mb-3 mx-auto" />

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
import { 
  HugeiconsIcon 
} from '@hugeicons/vue'
import { 
  UserCircleIcon, 
  BrainIcon, 
  Add01Icon, 
  Remove01Icon,
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

.top-nav {
  background: linear-gradient(135deg, #6A0DAD, #8A2BE2);
  box-shadow: 0 2px 15px rgba(0,0,0,0.1);
  z-index: 1000;
  padding: 1rem 0;
}

.top-nav .nav-link {
  color: rgba(255,255,255,0.8);
  border-radius: 15px;
  padding: 8px 16px;
  margin: 0 4px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  text-decoration: none;
}

.top-nav .nav-link:hover,
.top-nav .nav-link.active,
.top-nav .router-link-active {
  background-color: rgba(255,255,255,0.2);
  color: white;
  transform: translateY(-2px);
  text-decoration: none;
}

.top-nav .nav-link.logout-btn {
  background-color: #dc3545;
  color: white;
}

.top-nav .nav-link.logout-btn:hover {
  background-color: #c82333;
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
</style>
