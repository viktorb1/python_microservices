<template>
    <div>
        <div v-if="user">
            <h3>Account Information</h3>
            <form @submit.prevent="infoSubmit">
                <div class="mb-3">
                    <v-text-field label="First Name" v-model="infoData.first_name" />
                    <v-text-field label="Last Name" v-model="infoData.last_name" />
                    <v-text-field label="Email" v-model="infoData.email" />
                    <v-btn color="primary" type="submit">Save</v-btn>
                </div>
            </form>
            <h3 class="mt-4">Change Password</h3>
            <form @submit.prevent="passwordSubmit">
                <div class="mb-3">
                    <v-text-field label="Password" v-model="passwordData.password" />
                    <v-text-field label="Password Confirm" v-model="passwordData.password_confirm" />
                    <v-btn color="primary" type="submit">Save</v-btn>
                </div>
            </form>
        </div>
    </div>
</template>
<script setup lang="ts">
import axios from 'axios';
import { ref, reactive } from 'vue';
import { useUserStore } from "@/stores/userStore";
import { storeToRefs } from 'pinia';


const userStore = useUserStore()
const { user } = storeToRefs(userStore)

const infoData = reactive({
    first_name: user.value.first_name,
    last_name: user.value.last_name,
    email: user.value.email
})

const passwordData = reactive({
    password: "",
    password_confirm: "",
})

const infoSubmit = async () => {
    const updatedUser = {
        ...user.value,
        ...infoData
    };

    await axios.put("users/info", updatedUser, { withCredentials: true })
    userStore.setUser(updatedUser)
}

const passwordSubmit = async () => {
    await axios.put("users/password", passwordData)
}


</script>
