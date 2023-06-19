import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('userStore', () => {
  const user = ref(null)

  const setUser = (userData) => {
    user.value = userData
  }

  return { user, setUser }
})
