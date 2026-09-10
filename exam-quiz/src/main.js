import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import 'katex/dist/katex.min.css'
import './style.css'

// 路由配置
const routes = [
  { path: '/', component: () => import('./views/HomeView.vue') },
  { path: '/quiz', component: () => import('./views/QuizView.vue') },
  { path: '/wrongbook', component: () => import('./views/WrongBookView.vue') },
  { path: '/result', component: () => import('./views/ResultView.vue') }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')
