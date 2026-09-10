// localStorage 封装 - 刷题进度、答题记录、错题本持久化存储

const STORAGE_KEYS = {
  PROGRESS: 'exam_quiz_progress',      // 各板块进度map + lastActive
  ANSWERS: 'exam_quiz_answers',        // 答题记录
  WRONG: 'exam_quiz_wrong',            // 错题本
  SETTINGS: 'exam_quiz_settings'       // 设置
}

// 通用读取
function get(key, defaultValue = null) {
  try {
    const val = localStorage.getItem(key)
    return val ? JSON.parse(val) : defaultValue
  } catch (e) {
    return defaultValue
  }
}

// 通用写入
function set(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value))
    return true
  } catch (e) {
    return false
  }
}

// 生成板块唯一key
function makeProgressKey(bigSubject, mode, section) {
  return `${bigSubject}__${mode}__${section}`
}

// ===== 刷题进度 =====
// 结构：{ lastActive: {bigSubject,mode,section,currentIndex}, sections: { "key": {bigSubject,mode,section,currentIndex} } }
function getProgressStore() {
  const raw = get(STORAGE_KEYS.PROGRESS, null)
  // 兼容旧格式：直接是 {bigSubject, mode, section, currentIndex}
  if (raw && raw.bigSubject && raw.mode && raw.section !== undefined) {
    const key = makeProgressKey(raw.bigSubject, raw.mode, raw.section)
    return {
      lastActive: { ...raw },
      sections: { [key]: { ...raw } }
    }
  }
  // 新格式
  if (raw && raw.sections) return raw
  return { lastActive: null, sections: {} }
}

// 获取最近一次刷题进度（用于首页恢复提示）
export function getProgress() {
  const store = getProgressStore()
  return store.lastActive
}

// 获取指定板块的进度
export function getSectionProgress(bigSubject, mode, section) {
  const store = getProgressStore()
  const key = makeProgressKey(bigSubject, mode, section)
  return store.sections[key] || null
}

// 保存进度（同时更新板块进度和最近活跃）
export function setProgress(progress) {
  const store = getProgressStore()
  const key = makeProgressKey(progress.bigSubject, progress.mode, progress.section)
  store.sections[key] = { ...progress }
  store.lastActive = { ...progress }
  return set(STORAGE_KEYS.PROGRESS, store)
}

// 清除最近活跃进度（完成板块后调用，不清除各板块独立进度）
export function clearProgress() {
  const store = getProgressStore()
  store.lastActive = null
  return set(STORAGE_KEYS.PROGRESS, store)
}

// 清除指定板块的进度
export function clearSectionProgress(bigSubject, mode, section) {
  const store = getProgressStore()
  const key = makeProgressKey(bigSubject, mode, section)
  delete store.sections[key]
  // 如果清除的是lastActive，也清除lastActive
  if (store.lastActive &&
      store.lastActive.bigSubject === bigSubject &&
      store.lastActive.mode === mode &&
      store.lastActive.section === section) {
    store.lastActive = null
  }
  return set(STORAGE_KEYS.PROGRESS, store)
}

// 清除所有刷题记录（进度+答题记录），但保留错题本
export function clearAllQuizRecords() {
  localStorage.removeItem(STORAGE_KEYS.PROGRESS)
  localStorage.removeItem(STORAGE_KEYS.ANSWERS)
}

// ===== 答题记录 =====
// 结构：{ "公共基础": { "sectionKey": { "题目id": "用户答案" } }, "专业基础": {...} }
export function getAnswers() {
  return get(STORAGE_KEYS.ANSWERS, {})
}

export function saveAnswer(bigSubject, sectionKey, questionId, userAnswer) {
  const all = getAnswers()
  if (!all[bigSubject]) all[bigSubject] = {}
  if (!all[bigSubject][sectionKey]) all[bigSubject][sectionKey] = {}
  all[bigSubject][sectionKey][questionId] = userAnswer
  return set(STORAGE_KEYS.ANSWERS, all)
}

export function getSectionAnswers(bigSubject, sectionKey) {
  const all = getAnswers()
  return (all[bigSubject] && all[bigSubject][sectionKey]) || {}
}

export function clearSectionAnswers(bigSubject, sectionKey) {
  const all = getAnswers()
  if (all[bigSubject] && all[bigSubject][sectionKey]) {
    delete all[bigSubject][sectionKey]
    set(STORAGE_KEYS.ANSWERS, all)
  }
}

// ===== 错题本 =====
// 结构：{ "公共基础": [题目id数组], "专业基础": [题目id数组] }
export function getWrongBook() {
  const stored = get(STORAGE_KEYS.WRONG, {})
  return {
    '公共基础': stored['公共基础'] || [],
    '专业基础': stored['专业基础'] || []
  }
}

export function addWrong(bigSubject, questionId) {
  const wrong = getWrongBook()
  if (!wrong[bigSubject]) wrong[bigSubject] = []
  if (!wrong[bigSubject].includes(questionId)) {
    wrong[bigSubject].push(questionId)
    set(STORAGE_KEYS.WRONG, wrong)
  }
}

export function removeWrong(bigSubject, questionId) {
  const wrong = getWrongBook()
  if (wrong[bigSubject]) {
    wrong[bigSubject] = wrong[bigSubject].filter(id => id !== questionId)
    set(STORAGE_KEYS.WRONG, wrong)
  }
}

export function isWrong(bigSubject, questionId) {
  const wrong = getWrongBook()
  return wrong[bigSubject] && wrong[bigSubject].includes(questionId)
}

export function clearWrongBook(bigSubject) {
  const wrong = getWrongBook()
  wrong[bigSubject] = []
  set(STORAGE_KEYS.WRONG, wrong)
}
