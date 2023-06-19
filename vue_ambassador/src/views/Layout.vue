<template>
    <Navigation />

    <main>

        <Header v-if="showHeader" />

        <div class="album py-5 bg-body-tertiary">
            <div class="container">
                <router-view />
            </div>
        </div>
    </main>
</template>

<script setup lang="ts">
import Navigation from "@/components/Navigation.vue"
import Header from "@/components/Header.vue"

import { onMounted, computed } from "vue"
import { useUserStore } from "@/stores/userStore"
import { useRoute } from "vue-router"
import axios from "axios"

const userStore = useUserStore()

onMounted(async () => {
    try {
        const { data } = await axios.get("user")
        userStore.setUser(data)
    } catch (e) {
        userStore.setUser(null)
    }
})

const route = useRoute()
const showHeader = computed(() => route.path === '/' || route.path === '/backend')

</script>