<template>
  <div class="card dashboard-card quote-card">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-start mb-3">
        <h5 class="card-title mb-0">
          <i class="fas fa-quote-left me-2"></i>Daily Inspiration
        </h5>
        <button class="btn btn-sm btn-outline-secondary" @click="refreshQuote" :disabled="loading">
          <i class="fas fa-sync-alt" :class="{ 'fa-spin': loading }"></i>
        </button>
      </div>
      
      <div v-if="loading" class="text-center py-3">
        <div class="spinner-border spinner-border-sm text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      
      <div v-else-if="quote" class="quote-content">
        <blockquote class="blockquote mb-3">
          <p class="mb-2 fs-5">{{ quote.q }}</p>
          <footer class="blockquote-footer">
            <cite title="Source Title">{{ quote.a }}</cite>
          </footer>
        </blockquote>
        
        <div class="d-flex justify-content-between align-items-center">
          <small class="text-muted">
            <i class="fas fa-heart me-1"></i>
            {{ category }}
          </small>
          <button class="btn btn-sm btn-link text-primary p-0" @click="shareQuote">
            <i class="fas fa-share-alt"></i>
          </button>
        </div>
      </div>
      
      <div v-else class="text-center py-3 text-muted">
        <i class="fas fa-quote-left fa-2x mb-2"></i>
        <p>Unable to load quote</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { quotesService, type Quote } from '../services/quotes'

const quote = ref<Quote | null>(null)
const loading = ref(false)
const category = ref('Inspirational')

const refreshQuote = async () => {
  loading.value = true
  try {
    quote.value = await quotesService.getRandomQuote()
    // Simple categorization based on quote content
    if (quote.value) {
      const text = quote.value.q.toLowerCase()
      if (text.includes('love') || text.includes('heart')) {
        category.value = 'Love'
      } else if (text.includes('success') || text.includes('work')) {
        category.value = 'Success'
      } else if (text.includes('mind') || text.includes('think')) {
        category.value = 'Wisdom'
      } else {
        category.value = 'Inspirational'
      }
    }
  } catch (error) {
    console.error('Failed to refresh quote:', error)
  } finally {
    loading.value = false
  }
}

const shareQuote = () => {
  if (quote.value) {
    const text = `"${quote.value.q}" - ${quote.value.a}`
    if (navigator.share) {
      navigator.share({
        title: 'Inspirational Quote',
        text: text
      })
    } else {
      // Fallback: copy to clipboard
      navigator.clipboard.writeText(text)
      // Could add a toast notification here
    }
  }
}

onMounted(() => {
  refreshQuote()
})
</script>

<style scoped>
.quote-card {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.05), rgba(236, 72, 153, 0.05));
  border-left: 4px solid var(--primary-purple);
}

.quote-content {
  min-height: 120px;
}

.blockquote {
  border-left: none;
  padding-left: 0;
}

.card-title {
  color: var(--primary-purple);
}

.btn-outline-secondary:hover {
  color: var(--primary-purple);
  border-color: var(--primary-purple);
}

.fa-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
