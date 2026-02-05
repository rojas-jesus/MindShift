import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useDashboardStore = defineStore('dashboard', () => {
  // State
  const thoughts = ref([
    { id: 1, name: 'Morning Reflection', icon: 'Sun01Icon', status: true, color: 'yellow' },
    { id: 2, name: 'Gratitude Journal', icon: 'FavouriteIcon', status: true, color: 'pink' },
    { id: 3, name: 'Mood Tracker', icon: 'SmileIcon', status: false, color: 'blue' },
    { id: 4, name: 'Meditation', icon: 'NaturalFoodIcon', status: true, color: 'purple' }
  ])

  const mindTools = ref([
    { id: 5, name: 'Breathing Exercise', icon: 'FastWindIcon', status: true, color: 'light-blue' },
    { id: 6, name: 'Affirmations', icon: 'StarIcon', status: true, color: 'yellow' },
    { id: 7, name: 'Mindfulness', icon: 'BrainIcon', status: false, color: 'purple' },
    { id: 8, name: 'Sleep Tracker', icon: 'ZzzIcon', status: true, color: 'indigo' }
  ])


  const members = ref([
    { id: 1, name: 'Scarlett', role: 'Self Care', avatar: 'S' },
    { id: 2, name: 'Nariya', role: 'Support', avatar: 'N' },
    { id: 3, name: 'Riya', role: 'Support', avatar: 'R' },
    { id: 4, name: 'Dad', role: 'Mentor', avatar: 'D' },
    { id: 5, name: 'Mom', role: 'Guide', avatar: 'M' }
  ])

  const emotionalTemperature = ref(25) // 0-50 scale: 0=sad, 25=neutral, 50=happy
  const currentMood = ref({ level: 'Balanced', emoji: '😊', color: 'yellow' })

  // Mood history for chart
  const moodHistory = ref([
    { day: 'Mon', mood: 35, emotion: 'Happy' },
    { day: 'Tue', mood: 20, emotion: 'Sad' },
    { day: 'Wed', mood: 15, emotion: 'Anxious' },
    { day: 'Thu', mood: 30, emotion: 'Calm' },
    { day: 'Fri', mood: 40, emotion: 'Happy' },
    { day: 'Sat', mood: 45, emotion: 'Excited' },
    { day: 'Sun', mood: 38, emotion: 'Content' }
  ])

  // Actions
  const toggleThought = (thoughtId: number) => {
    const thought = thoughts.value.find(t => t.id === thoughtId)
    if (thought) {
      thought.status = !thought.status
    }
  }

  const toggleMindTool = (toolId: number) => {
    const tool = mindTools.value.find(t => t.id === toolId)
    if (tool) {
      tool.status = !tool.status
    }
  }

  const setEmotionalTemperature = (newTemp: number) => {
    emotionalTemperature.value = Math.max(0, Math.min(50, newTemp))
    updateMood()
  }

  const updateMood = () => {
    const temp = emotionalTemperature.value
    if (temp < 15) {
      currentMood.value = { level: 'Sad', emoji: '😢', color: 'blue' }
    } else if (temp < 25) {
      currentMood.value = { level: 'Anxious', emoji: '😰', color: 'orange' }
    } else if (temp < 35) {
      currentMood.value = { level: 'Balanced', emoji: '😊', color: 'yellow' }
    } else {
      currentMood.value = { level: 'Happy', emoji: '😄', color: 'green' }
    }
  }

  return {
    thoughts,
    mindTools,
    members,
    emotionalTemperature,
    currentMood,
    moodHistory,
    toggleThought,
    toggleMindTool,
    setEmotionalTemperature,
    updateMood
  }
})
