<template>
    <main class="form-signin w-100 m-auto">
        <form @submit.prevent="submit">
            <h1 class="h3 mb-3 fw-normal">Please register</h1>

            <div class="form-floating">
                <input v-model="data.first_name" class="form-control" placeholder="First Name">
                <label>First name</label>
            </div>
            <div class="form-floating">
                <input v-model="data.last_name" class="form-control" placeholder="Last Name">
                <label>Last name</label>
            </div>
            <div class="form-floating">
                <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com">
                <label>Email address</label>
            </div>
            <div class="form-floating">
                <input v-model="data.password" type="password1" class="form-control" placeholder="Password">
                <label>Password</label>
            </div>
            <div class="form-floating">
                <input v-model="data.password_confirm" type="password" class="form-control" placeholder="Password Confirm">
                <label>Password Confirm</label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
        </form>
    </main>
</template>


<script setup lang="ts">
import { reactive } from "vue"
import axios from "axios"
import { useRouter } from "vue-router";

const router = useRouter()

const data = reactive({
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": "",
    "password_confirm": ""
})

const submit = async () => {
    await axios.post("register", {
        first_name: data.first_name,
        last_name: data.last_name,
        email: data.email,
        password: data.password,
        password_confirm: data.password_confirm
    })

    await router.push("/login")
}
</script>

<style scoped>
.form-signin {
    max-width: 330px;
    padding: 15px;
}

.form-signin .form-floating:focus-within {
    z-index: 2;
}

.form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>