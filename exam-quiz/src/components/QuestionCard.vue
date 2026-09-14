<template>
  <div class="question-card">
    <div class="question-header">
      <span class="q-num">{{ question.year }}-{{ question.yearQnum || question.id }}</span>
      <span class="q-progress">{{ currentIndex + 1 }} / {{ total }}</span>
      <span class="q-subject">{{ question.smallSubject }}</span>
    </div>

    <div class="question-content" v-html="renderedQuestion"></div>

    <div class="options">
      <button
        v-for="opt in ['A', 'B', 'C', 'D']"
        :key="opt"
        class="option-btn"
        :class="{
          selected: selectedAnswer === opt,
          correct: locked && question.answer === opt,
          wrong: locked && selectedAnswer === opt && question.answer !== opt,
          disabled: locked
        }"
        :disabled="locked"
        @click="selectOption(opt)"
      >
        <span class="opt-label">{{ opt }}</span>
        <span class="opt-content" v-html="renderOption(opt)"></span>
      </button>
    </div>

    <div class="submit-area">
      <button
        class="submit-btn"
        :disabled="!selectedAnswer || locked"
        @click="$emit('submit')"
      >
        提交答案
      </button>
      <button
        v-if="locked"
        class="analysis-btn"
        @click="$emit('analysis')"
      >
        查看解析
      </button>
      <button
        v-if="locked"
        class="next-btn"
        @click="$emit('next')"
      >
        {{ isLast ? '查看结果' : '下一题' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import katex from 'katex'

const props = defineProps({
  question: { type: Object, required: true },
  currentIndex: { type: Number, default: 0 },
  total: { type: Number, default: 0 },
  locked: { type: Boolean, default: false },
  initialAnswer: { type: String, default: '' }
})

const emit = defineEmits(['submit', 'next', 'select', 'analysis'])

const selectedAnswer = ref(props.initialAnswer || '')

watch(() => props.question, () => {
  selectedAnswer.value = props.initialAnswer || ''
})

watch(() => props.initialAnswer, (val) => {
  selectedAnswer.value = val || ''
})

const isLast = computed(() => props.currentIndex === props.total - 1)

// 渲染LaTeX公式
function renderLatex(text) {
  if (!text) return ''
  // 处理 $...$ 公式
  return text.replace(/\$([^$]+)\$/g, (match, formula) => {
    try {
      return katex.renderToString(formula, {
        throwOnError: false,
        displayMode: false
      })
    } catch (e) {
      return match
    }
  })
}

const renderedQuestion = computed(() => {
  return renderLatex(props.question.question || '')
})

function renderOption(opt) {
  return renderLatex(props.question[opt] || '')
}

function selectOption(opt) {
  if (props.locked) return
  selectedAnswer.value = opt
  emit('select', opt)
}
</script>

<style scoped>
.question-card {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}

.question-header {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.q-num {
  background: #4a90d9;
  color: #fff;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 13px;
}

.q-progress {
  color: #888;
  font-size: 13px;
  padding: 2px 8px;
}

.q-subject, .q-year {
  color: #666;
  font-size: 13px;
  padding: 2px 8px;
  background: #f0f0f0;
  border-radius: 12px;
}

.question-content {
  font-size: 16px;
  line-height: 1.8;
  color: #333;
  margin-bottom: 20px;
  word-break: break-word;
}

.question-content :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
  margin: 8px 0;
}

.question-content :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0;
}

.question-content :deep(td), .question-content :deep(th) {
  border: 1px solid #ddd;
  padding: 6px 10px;
  text-align: center;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.option-btn {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  background: #fff;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
  font-size: 15px;
  line-height: 1.6;
}

.option-btn:hover:not(:disabled) {
  border-color: #4a90d9;
  background: #f0f7ff;
}

.option-btn.selected {
  border-color: #4a90d9;
  background: #e8f2ff;
}

.option-btn.correct {
  border-color: #52c41a;
  background: #f6ffed;
}

.option-btn.wrong {
  border-color: #ff4d4f;
  background: #fff2f0;
}

.option-btn:disabled {
  cursor: not-allowed;
}

.opt-label {
  font-weight: bold;
  color: #4a90d9;
  min-width: 24px;
}

.option-btn.correct .opt-label {
  color: #52c41a;
}

.option-btn.wrong .opt-label {
  color: #ff4d4f;
}

.opt-content {
  flex: 1;
  word-break: break-word;
}

.opt-content :deep(img) {
  max-width: 100%;
  height: auto;
}

.submit-area {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.submit-btn, .next-btn, .analysis-btn {
  padding: 12px 36px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.2s;
}

.submit-btn {
  background: #4a90d9;
  color: #fff;
}

.submit-btn:hover:not(:disabled) {
  background: #357abd;
}

.submit-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.next-btn {
  background: #52c41a;
  color: #fff;
}

.next-btn:hover {
  background: #389e0d;
}

.analysis-btn {
  background: #fff;
  color: #4a90d9;
  border: 1px solid #4a90d9;
}

.analysis-btn:hover {
  background: #4a90d9;
  color: #fff;
}

@media (max-width: 600px) {
  .question-card {
    padding: 14px;
  }
  .question-content {
    font-size: 15px;
  }
  .option-btn {
    padding: 12px;
    font-size: 14px;
  }
  .submit-btn, .next-btn, .analysis-btn {
    padding: 10px 24px;
    font-size: 15px;
    flex: 1;
  }
}
</style>
