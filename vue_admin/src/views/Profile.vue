<template>
    <div>
        <h3>Account Information</h3>
        <form @submit.prevent="infoSubmit">
            <div class="mb-3">
                <v-text-field label="First Name" v-model="userStore.user.first_name" />
                <v-text-field label="Last Name" v-model="userStore.user.last_name" />
                <v-text-field label="Email" v-model="userStore.user.email" />
                <v-btn color="primary" type="submit">Save</v-btn>
            </div>
        </form>
        <h3 class="mt-4">Change Password</h3>
        <form @submit.prevent="passwordSubmit">
            <div class="mb-3">
                <v-text-field label="Password" v-model="password" />
                <v-text-field label="Password Confirm" v-model="password_confirm" />
                <v-text-field label="Email" v-model="userStore.user.email" />
                <v-btn color="primary" type="submit">Save</v-btn>
            </div>
        </form>
    </div>
</template>
<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from "@/stores/userStore";


const password = ref("")
const password_confirm = ref("")
const userStore = useUserStore()

const infoSubmit = async () => {
    const new_val = {
        first_name: userStore.user.first_name,
        last_name: userStore.user.last_name,
        email: userStore.user.email
    }

    await axios.put("users/info", new_val, { withCredentials: true })
    userStore.setUser(new_val)
}

const passwordSubmit = async () => {
    await axios.put("users/password", {
        password: password.value,
        password_confirm: password_confirm.value,
    })
}

</script>
