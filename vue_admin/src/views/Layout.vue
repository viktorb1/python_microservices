<template>
    <v-app>
        <Nav />
        <div class="container-fluid">
            <div class="row">
                <Menu />

                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">

                    <div class="table-responsive">
                        <router-view />
                    </div>
                </main>
            </div>
        </div>
    </v-app>
</template>

<script setup lang="ts">

import Nav from "@/components/Nav.vue"
import Menu from "@/components/Menu.vue"
import { onMounted, ref } from 'vue'
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/userStore";
import axios from "axios"

const router = useRouter()
const userStore = useUserStore()

onMounted(async () => {
    try {
        const { data } = await axios.get("user", { withCredentials: true })
        userStore.setUser(data)
    } catch (e) {
        await router.push("/login")
    }
})

</script>