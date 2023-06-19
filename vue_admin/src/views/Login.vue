<template>
    <main class="form-signin w-100 m-auto">
        <form @submit.prevent="submit">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating">
                <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com">
                <label>Email address</label>
            </div>
            <div class="form-floating">
                <input v-model="data.password" type="password" class="form-control" placeholder="Password">
                <label>Password</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        </form>
    </main>
</template>


<script setup lang="ts">
import { reactive } from "vue"
import axios from "axios"
import { useRouter } from "vue-router";

const router = useRouter()

const data = reactive({
    "email": "",
    "password": "",
})

const submit = async () => {
    await axios.post("login", {
        email: data.email,
        password: data.password,
    }, { withCredentials: true })

    await router.push("/")
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