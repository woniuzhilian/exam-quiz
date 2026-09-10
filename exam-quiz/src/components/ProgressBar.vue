<template>
  <div class="progress-bar">
    <div class="progress-info">
      <span>{{ current }} / {{ total }}</span>
      <span>{{ percent }}%</span>
    </div>
    <div class="progress-track">
      <div class="progress-fill" :style="{ width: percent + '%' }"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  current: { type: Number, default: 0 },
  total: { type: Number, default: 0 }
})

const percent = computed(() => {
  if (props.total === 0) return 0
  return Math.round((props.current / props.total) * 100)
})
</script>

<style scoped>
.progress-bar {
  margin-bottom: 16px;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: #666;
  margin-bottom: 6px;
}

.progress-track {
  height: 8px;
  background: #e8e8e8;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4a90d9, #6ab0f3);
  border-radius: 4px;
  transition: width 0.3s ease;
}
</style>
