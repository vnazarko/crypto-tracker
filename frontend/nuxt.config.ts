// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/ui', 'nuxt-telegram-auth'],
  ui: {
    global: true,
  },
  css: ['assets/sass/main.sass'],
  runtimeConfig: {
    TELEGRAM_TOKEN: process.env.NUXT_ENV_TELEGRAM_TOKEN
  }
})