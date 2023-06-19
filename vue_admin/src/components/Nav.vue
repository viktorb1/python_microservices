<template>
    <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
        <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6" href="#">Admin Panel</a>

        <nav class="my-2 my-md-0 mr-md-3">
            <router-link to="/profile" class="p-2 text-white text-decoration-none">Hello, {{ user.first_name }} {{
                user.last_name }}
            </router-link>
            <a href="#" class="p-2 text-white text-decoration-none" @click="logout">Sign out</a>
        </nav>
    </header>
</template>

<script setup lang="ts">

import axios from "axios"
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";

interface User {
    id: number;
    first_name: string;
    last_name: string;
    email: string;
    is_ambassador: boolean;
}

const router = useRouter()
const userStore = useUserStore()
const { user } = storeToRefs(userStore)

const logout = async () => {
    await axios.post("logout", {}, { withCredentials: true })
    await router.push("/login")
}

</script>