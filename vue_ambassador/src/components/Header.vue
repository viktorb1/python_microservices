<template>
    <section class="py-5 text-center container">
        <div class="row py-lg-5">
            <div class="col-lg-6 col-md-8 mx-auto">
                <h1 class="fw-light">{{ title }}</h1>
                <p class="lead text-body-secondary">{{ description }}
                </p>
                <p v-if="!user">
                    <router-link to="/login" class="btn btn-primary my-2 mx-2">Login</router-link>
                    <router-link to="/register" class="btn btn-secondary my-2">Register</router-link>
                </p>

            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { useUserStore } from "@/stores/userStore";
import { ref, computed } from "vue"
import { storeToRefs } from "pinia"

const userStore = useUserStore()
const { user } = storeToRefs(userStore)

const title = computed(() => user.value ? "$" + user.value.revenue : "Welcome")
const description = computed(() => user.value ? "You have earned this far" : "Share links to earn money")
</script>