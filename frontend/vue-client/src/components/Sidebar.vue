<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { HugeiconsIcon } from '@hugeicons/vue'
import { 
  Menu01Icon,
  Search01Icon,
  Layout01Icon as DashboardIcon,
  Note01Icon,
  InformationCircleIcon,
  Idea01Icon as ActionIcon
} from '@hugeicons/core-free-icons'

const props = defineProps<{
  isCollapsed: boolean
}>()

const emit = defineEmits(['toggle'])

const menuItems = [
  { name: 'Dashboard', icon: DashboardIcon, path: '/dashboard' },
  { name: 'Thoughts', icon: Note01Icon, path: '/thoughts' },
  { name: 'Raw Actions', icon: ActionIcon, path: '/action-raw/create' },
  { name: 'About', icon: InformationCircleIcon, path: '/about' },
]
</script>

<template>
  <aside 
    class="sidebar" 
    :class="{ 'collapsed': isCollapsed }"
  >
    <div class="sidebar-header">
      <div class="logo-container" v-if="!isCollapsed">
        <div class="logo-icon">M</div>
        <span class="logo-text">MindShift</span>
      </div>
      <div class="logo-container collapsed" v-else>
         <div class="logo-icon">M</div>
      </div>
    </div>

    <div class="sidebar-content">
      <div class="search-box" v-if="!isCollapsed">
        <HugeiconsIcon :icon="Search01Icon" size="18" class="search-icon" />
        <input type="text" placeholder="Buscar..." />
      </div>
      <div class="search-box-collapsed" v-else>
        <HugeiconsIcon :icon="Search01Icon" size="24" class="search-icon" />
      </div>

      <nav class="sidebar-nav">
        <RouterLink 
          v-for="item in menuItems" 
          :key="item.path"
          :to="item.path"
          class="nav-item"
          :title="isCollapsed ? item.name : ''"
        >
          <HugeiconsIcon :icon="item.icon" size="24" class="item-icon" />
          <span v-if="!isCollapsed" class="item-text">{{ item.name }}</span>
        </RouterLink>
      </nav>
    </div>

    <div class="sidebar-footer">
      <!-- You can add more footer items here if needed -->
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 260px;
  height: 100vh;
  background: white;
  border-right: 1px solid #edf2f7;
  display: flex;
  flex-direction: column;
  transition: width 0.3s ease;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1001;
}

.sidebar.collapsed {
  width: 80px;
}

.sidebar-header {
  padding: 24px;
  height: 80px;
  display: flex;
  align-items: center;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-container.collapsed {
  justify-content: center;
  width: 100%;
}

.logo-icon {
  width: 32px;
  height: 32px;
  background: #f15a24; /* Apex-like color but let's use MindShift's flow */
  background: linear-gradient(135deg, #f15a24, #d4145a);
  color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a202c;
  letter-spacing: -0.5px;
}

.sidebar-content {
  flex: 1;
  padding: 0 16px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.search-box {
  background: #f7fafc;
  border-radius: 12px;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-box-collapsed {
  display: flex;
  justify-content: center;
  padding: 10px 0;
  color: #a0aec0;
}

.search-icon {
  color: #a0aec0;
}

.search-box input {
  border: none;
  background: transparent;
  width: 100%;
  font-size: 0.9rem;
  color: #4a5568;
}

.search-box input:focus {
  outline: none;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 16px;
  border-radius: 12px;
  color: #718096;
  text-decoration: none;
  transition: all 0.2s ease;
}

.nav-item:hover {
  background: #f7fafc;
  color: #4a5568;
}

.nav-item.router-link-active {
  background: #f0f4ff;
  color: #4c51bf;
}

.collapsed .nav-item {
  justify-content: center;
  padding: 12px 0;
}

.item-icon {
  flex-shrink: 0;
}

.item-text {
  font-weight: 500;
  white-space: nowrap;
}

.sidebar-footer {
  padding: 16px;
}
</style>
