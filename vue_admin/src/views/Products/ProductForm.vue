<template>
    <form @submit.prevent="submit">
        <div class="mb-3">
            <v-text-field label="Title" v-model="title" />
            <v-textarea labe="Description" v-model="description" />

            <v-text-field label="Image" v-model="image" />
            <v-text-field label="Price" type="number" min="0" v-model="price" />
            <v-btn color="primary" type="submit">Save</v-btn>
        </div>
    </form>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import axios from "axios"
import { useRouter, useRoute } from "vue-router";

const title = ref("")
const description = ref("")
const image = ref("")
const price = ref("")
const router = useRouter()
const route = useRoute()

const submit = async () => {
    console.log("this is running")

    if (route.params.id) {
        await axios.put(`products/${route.params.id}`, {
            title: title.value,
            description: description.value,
            image: image.value,
            price: price.value
        }, { withCredentials: true })
    } else {
        await axios.post("products", {
            title: title.value,
            description: description.value,
            image: image.value,
            price: price.value
        }, { withCredentials: true })
    }


    await router.push("/products")
}

onMounted(async () => {
    if (route.params.id) {
        const { data } = await axios.get(`products/${route.params.id}`, { withCredentials: true })
        title.value = data.title
        description.value = data.description
        image.value = data.image
        price.value = data.price

    }
})

</script>
