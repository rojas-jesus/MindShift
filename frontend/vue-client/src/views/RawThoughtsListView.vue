<template>
  <div class="raw-thoughts-list-view">
    <div class="container-fluid p-4">
      <!-- Header -->
      <div class="row mb-4">
        <div class="col-12">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h2 class="page-title">
                <HugeiconsIcon :icon="Note01Icon" class="me-3" size="32" />
                Raw Thoughts Library
              </h2>
              <p class="text-muted">View, edit, and manage all your raw thought entries</p>
            </div>
            <RouterLink to="/thought-raw/create" class="btn btn-primary">
              <HugeiconsIcon :icon="Add01Icon" class="me-2" />
              New Thought
            </RouterLink>
          </div>
        </div>
      </div>

      <!-- Search and Filter -->
      <div class="row mb-4">
        <div class="col-md-6">
          <div class="search-box">
            <HugeiconsIcon :icon="Search01Icon" size="20" class="search-icon" />
            <input 
              v-model="searchQuery" 
              type="text" 
              placeholder="Search thoughts..." 
              class="form-control"
            />
          </div>
        </div>
      </div>

      <!-- Table -->
      <div class="row">
        <div class="col-12">
          <div class="table-card">
            <div v-if="loading" class="text-center py-5">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>

            <div v-else-if="filteredThoughts.length === 0" class="text-center py-5 text-muted">
              <HugeiconsIcon :icon="Note01Icon" size="48" class="mb-3 opacity-50" />
              <p>{{ searchQuery ? 'No thoughts match your search' : 'No thoughts found. Create your first one!' }}</p>
            </div>

            <div v-else class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th style="width: 80px">ID</th>
                    <th>Transcription</th>
                    <th style="width: 200px">Date</th>
                    <th style="width: 150px" class="text-center">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="thought in paginatedThoughts" :key="thought.id">
                    <td class="align-middle">
                      <span class="badge bg-light text-dark">#{{ thought.id }}</span>
                    </td>
                    <td class="align-middle">
                      <div class="transcription-cell" :title="thought.transcription">
                        {{ truncateText(thought.transcription, 100) }}
                      </div>
                    </td>
                    <td class="align-middle">
                      <small class="text-muted">{{ formatDate(thought.timestamp) }}</small>
                    </td>
                    <td class="align-middle text-center">
                      <div class="action-buttons">
                        <button 
                          @click="openEditModal(thought)" 
                          class="btn btn-sm btn-outline-primary"
                          title="Edit"
                        >
                          <HugeiconsIcon :icon="Edit01Icon" size="16" />
                        </button>
                        <button 
                          @click="confirmDelete(thought)" 
                          class="btn btn-sm btn-outline-danger"
                          title="Delete"
                        >
                          <HugeiconsIcon :icon="Delete01Icon" size="16" />
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Pagination -->
            <div v-if="totalPages > 1" class="pagination-container">
              <nav>
                <ul class="pagination justify-content-center mb-0">
                  <li class="page-item" :class="{ disabled: currentPage === 1 }">
                    <button class="page-link" @click="currentPage--" :disabled="currentPage === 1">
                      Previous
                    </button>
                  </li>
                  <li 
                    v-for="page in totalPages" 
                    :key="page"
                    class="page-item" 
                    :class="{ active: currentPage === page }"
                  >
                    <button class="page-link" @click="currentPage = page">{{ page }}</button>
                  </li>
                  <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                    <button class="page-link" @click="currentPage++" :disabled="currentPage === totalPages">
                      Next
                    </button>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Modal -->
    <div v-if="showEditModal" class="modal-overlay" @click.self="closeEditModal">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Edit Raw Thought</h5>
            <button type="button" class="btn-close" @click="closeEditModal"></button>
          </div>
          <div class="modal-body">
            <div class="mb-3">
              <label class="form-label">Transcription</label>
              <textarea 
                v-model="editingThought.transcription" 
                class="form-control" 
                rows="6"
                placeholder="Enter your thought..."
              ></textarea>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeEditModal">Cancel</button>
            <button type="button" class="btn btn-primary" @click="saveEdit" :disabled="saving">
              <span v-if="saving" class="spinner-border spinner-border-sm me-2"></span>
              {{ saving ? 'Saving...' : 'Save Changes' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="modal-overlay" @click.self="closeDeleteModal">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirm Delete</h5>
            <button type="button" class="btn-close" @click="closeDeleteModal"></button>
          </div>
          <div class="modal-body">
            <p>Are you sure you want to delete this thought? This action cannot be undone.</p>
            <div class="alert alert-warning">
              <strong>Thought #{{ deletingThought?.id }}</strong>
              <p class="mb-0 mt-2">{{ truncateText(deletingThought?.transcription || '', 150) }}</p>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeDeleteModal">Cancel</button>
            <button type="button" class="btn btn-danger" @click="deleteThought" :disabled="deleting">
              <span v-if="deleting" class="spinner-border spinner-border-sm me-2"></span>
              {{ deleting ? 'Deleting...' : 'Delete' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { HugeiconsIcon } from '@hugeicons/vue'
import { 
  Note01Icon,
  Add01Icon,
  Search01Icon,
  PencilEdit01Icon as Edit01Icon,
  Delete01Icon
} from '@hugeicons/core-free-icons'
import { thoughtRawService, type ThoughtRawEntry } from '../services/thoughtRaw'

const thoughts = ref<ThoughtRawEntry[]>([])
const loading = ref(true)
const searchQuery = ref('')
const currentPage = ref(1)
const itemsPerPage = 10

const showEditModal = ref(false)
const editingThought = ref<ThoughtRawEntry>({ id: 0, transcription: '', timestamp: '' })
const saving = ref(false)

const showDeleteModal = ref(false)
const deletingThought = ref<ThoughtRawEntry | null>(null)
const deleting = ref(false)

const filteredThoughts = computed(() => {
  if (!searchQuery.value) return thoughts.value
  const query = searchQuery.value.toLowerCase()
  return thoughts.value.filter(t => 
    t.transcription.toLowerCase().includes(query) ||
    t.id.toString().includes(query)
  )
})

const totalPages = computed(() => 
  Math.ceil(filteredThoughts.value.length / itemsPerPage)
)

const paginatedThoughts = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredThoughts.value.slice(start, end)
})

const truncateText = (text: string, maxLength: number) => {
  if (text.length <= maxLength) return text
  return text.substring(0, maxLength) + '...'
}

const formatDate = (timestamp: string) => {
  const date = new Date(timestamp)
  return date.toLocaleString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const openEditModal = (thought: ThoughtRawEntry) => {
  editingThought.value = { ...thought }
  showEditModal.value = true
}

const closeEditModal = () => {
  showEditModal.value = false
  editingThought.value = { id: 0, transcription: '', timestamp: '' }
}

const saveEdit = async () => {
  if (!editingThought.value.transcription.trim()) {
    alert('Transcription cannot be empty')
    return
  }

  saving.value = true
  try {
    await thoughtRawService.updateThoughtRaw(
      editingThought.value.id, 
      editingThought.value.transcription
    )
    
    // Update local state
    const index = thoughts.value.findIndex(t => t.id === editingThought.value.id)
    if (index !== -1) {
      thoughts.value[index].transcription = editingThought.value.transcription
    }
    
    closeEditModal()
  } catch (error) {
    console.error('Failed to update thought:', error)
    alert('Failed to update thought. Please try again.')
  } finally {
    saving.value = false
  }
}

const confirmDelete = (thought: ThoughtRawEntry) => {
  deletingThought.value = thought
  showDeleteModal.value = true
}

const closeDeleteModal = () => {
  showDeleteModal.value = false
  deletingThought.value = null
}

const deleteThought = async () => {
  if (!deletingThought.value) return

  deleting.value = true
  try {
    await thoughtRawService.deleteThoughtRaw(deletingThought.value.id)
    
    // Remove from local state
    thoughts.value = thoughts.value.filter(t => t.id !== deletingThought.value!.id)
    
    closeDeleteModal()
  } catch (error) {
    console.error('Failed to delete thought:', error)
    alert('Failed to delete thought. Please try again.')
  } finally {
    deleting.value = false
  }
}

onMounted(async () => {
  try {
    thoughts.value = await thoughtRawService.getAllThoughtRaw()
    thoughts.value.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime())
  } catch (error) {
    console.error('Failed to load thoughts:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.raw-thoughts-list-view {
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

.search-box {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 16px;
  color: #9ca3af;
  pointer-events: none;
}

.search-box input {
  padding-left: 48px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  height: 48px;
}

.search-box input:focus {
  border-color: #8B5CF6;
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
}

.table-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.table {
  margin-bottom: 0;
}

.table thead th {
  border-bottom: 2px solid #e5e7eb;
  color: #6b7280;
  font-weight: 600;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 16px;
}

.table tbody td {
  padding: 16px;
  vertical-align: middle;
}

.table tbody tr {
  border-bottom: 1px solid #f3f4f6;
  transition: background-color 0.2s;
}

.table tbody tr:hover {
  background-color: #f9fafb;
}

.transcription-cell {
  max-width: 500px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.action-buttons {
  display: flex;
  gap: 8px;
  justify-content: center;
}

.pagination-container {
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #e5e7eb;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1050;
  animation: fadeIn 0.2s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-dialog {
  max-width: 600px;
  width: 90%;
  animation: slideUp 0.3s;
}

@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.modal-content {
  border-radius: 16px;
  border: none;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}

.modal-header {
  border-bottom: 1px solid #e5e7eb;
  padding: 20px 24px;
}

.modal-title {
  font-weight: 600;
  color: #1a202c;
}

.modal-body {
  padding: 24px;
}

.modal-footer {
  border-top: 1px solid #e5e7eb;
  padding: 16px 24px;
}

textarea.form-control {
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  resize: vertical;
}

textarea.form-control:focus {
  border-color: #8B5CF6;
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
}
</style>
