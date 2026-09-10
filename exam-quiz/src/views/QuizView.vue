<template>
  <div class="quiz-page">
    <!-- 顶部导航 -->
    <div class="quiz-header">
      <button class="back-btn" @click="goHome">← 返回</button>
      <div class="quiz-info">
        <span class="big-subject">{{ bigSubject }}</span>
        <span class="divider">|</span>
        <span class="section">{{ section }}</span>
      </div>
    </div>

    <!-- 进度条 -->
    <ProgressBar :current="currentIndex + 1" :total="questions.length" />

    <!-- 题目卡片 -->
    <QuestionCard
      v-if="currentQuestion"
      :question="currentQuestion"
      :current-index="currentIndex"
      :total="questions.length"
      :locked="isLocked"
      :initial-answer="currentUserAnswer"
      :is-last="currentIndex === questions.length - 1"
      @submit="handleSubmit"
      @next="handleNext"
      @select="handleSelect"
    />

    <!-- 空状态 -->
    <div v-else class="empty-state">
      <div class="empty-icon">📭</div>
      <p>暂无题目</p>
      <button class="back-home-btn" @click="goHome">返回首页</button>
    </div>

    <!-- 答案解析弹窗 -->
    <ResultModal
      :visible="showModal"
      :question="currentQuestion"
      :user-answer="selectedAnswer"
      :is-last="currentIndex === questions.length - 1"
      @close="closeModal"
      @next="handleNext"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import QuestionCard from '../components/QuestionCard.vue'
import ResultModal from '../components/ResultModal.vue'
import ProgressBar from '../components/ProgressBar.vue'
import {
  getQuestionsBySmallSubject,
  getQuestionsByYear,
  getQuestionsByIds,
  makeSectionKey
} from '../utils/quiz'
import {
  getSectionProgress, setProgress, clearSectionProgress,
  saveAnswer, getSectionAnswers, clearSectionAnswers,
  addWrong, getWrongBook
} from '../utils/storage'

const route = useRoute()
const router = useRouter()

const bigSubject = ref(route.query.bigSubject || '')
const mode = ref(route.query.mode || '')
const section = ref(route.query.section || '')
const questions = ref([])
const currentIndex = ref(0)
const selectedAnswer = ref('')
const isLocked = ref(false)
const showModal = ref(false)

const sectionKey = computed(() => makeSectionKey(mode.value, section.value))

const currentQuestion = computed(() => questions.value[currentIndex.value])

const currentUserAnswer = computed(() => {
  if (!currentQuestion.value) return ''
  const answers = getSectionAnswers(bigSubject.value, sectionKey.value)
  return answers[currentQuestion.value.id] || ''
})

onMounted(() => {
  loadQuestions()
})

watch(() => route.query, () => {
  bigSubject.value = route.query.bigSubject || ''
  mode.value = route.query.mode || ''
  section.value = route.query.section || ''
  loadQuestions()
}, { deep: true })

function loadQuestions() {
  if (mode.value === 'smallSubject') {
    questions.value = getQuestionsBySmallSubject(bigSubject.value, section.value)
  } else if (mode.value === 'year') {
    questions.value = getQuestionsByYear(bigSubject.value, section.value)
  } else if (mode.value === 'wrong') {
    // 错题练习模式：清除之前的答题记录，允许重新作答
    clearSectionAnswers(bigSubject.value, sectionKey.value)
    const wrong = getWrongBook()
    const ids = wrong[bigSubject.value] || []
    questions.value = getQuestionsByIds(bigSubject.value, ids)
  }

  // 恢复该板块的独立进度（每个大科目+模式+板块各自保存进度）
  const sectionProgress = getSectionProgress(bigSubject.value, mode.value, section.value)
  if (sectionProgress) {
    currentIndex.value = sectionProgress.currentIndex || 0
  } else {
    currentIndex.value = 0
  }

  // 支持从指定题目开始（错题本单题练习）
  if (route.query.startIndex) {
    currentIndex.value = parseInt(route.query.startIndex) || 0
  }

  // 恢复当前题的答题状态
  restoreAnswerState()
}

function restoreAnswerState() {
  const answers = getSectionAnswers(bigSubject.value, sectionKey.value)
  if (currentQuestion.value && answers[currentQuestion.value.id]) {
    selectedAnswer.value = answers[currentQuestion.value.id]
    isLocked.value = true
  } else {
    selectedAnswer.value = ''
    isLocked.value = false
  }
}

function handleSelect(answer) {
  selectedAnswer.value = answer
}

function handleSubmit() {
  if (!selectedAnswer.value || isLocked.value) return

  isLocked.value = true

  // 保存答题记录
  saveAnswer(bigSubject.value, sectionKey.value, currentQuestion.value.id, selectedAnswer.value)

  // 答错加入错题本
  if (selectedAnswer.value !== currentQuestion.value.answer) {
    addWrong(bigSubject.value, currentQuestion.value.id)
  }

  // 保存进度
  setProgress({
    bigSubject: bigSubject.value,
    mode: mode.value,
    section: section.value,
    currentIndex: currentIndex.value
  })

  // 显示弹窗
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

function handleNext() {
  showModal.value = false

  if (currentIndex.value >= questions.value.length - 1) {
    // 完成所有题目，跳转到结果页
    router.push({
      path: '/result',
      query: {
        bigSubject: bigSubject.value,
        mode: mode.value,
        section: section.value
      }
    })
    return
  }

  currentIndex.value++
  restoreAnswerState()

  // 更新进度
  setProgress({
    bigSubject: bigSubject.value,
    mode: mode.value,
    section: section.value,
    currentIndex: currentIndex.value
  })
}

function goHome() {
  router.push('/')
}
</script>

<style scoped>
.quiz-page {
  max-width: 720px;
  margin: 0 auto;
  padding: 16px;
  min-height: 100vh;
}

.quiz-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
  gap: 12px;
}

.back-btn {
  background: none;
  border: none;
  color: #4a90d9;
  font-size: 15px;
  cursor: pointer;
  padding: 6px 0;
}

.quiz-info {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #666;
}

.big-subject {
  font-weight: bold;
  color: #333;
}

.divider {
  margin: 0 8px;
  color: #ccc;
}

@media (max-width: 600px) {
  .quiz-page {
    padding: 12px;
  }
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
  background: #fff;
  border-radius: 12px;
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.empty-state p {
  color: #888;
  font-size: 16px;
  margin-bottom: 20px;
}

.back-home-btn {
  padding: 10px 30px;
  background: #4a90d9;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  cursor: pointer;
}
</style>
