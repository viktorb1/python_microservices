import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('userStore', () => {
  const user = ref({
    email: '',
    first_name: '',
    id: '',
    is_ambassador: false,
    last_name: ''
  })

  const setUser = (userData) => {
    user.value = userData
  }

  return { user, setUser }
})
