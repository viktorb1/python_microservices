<template>
    <div class="container">
        <main>
            <div class="py-5 text-center">
                <h2>Success</h2>
                <p class="lead">Your purchase has been completed!</p>
            </div>
        </main>
    </div>
</template>

<script setup lang="ts">
const route = useRoute()

const { data } = await useAPIFetch('orders/confirm', {
    method: "POST",
    body: {
        source: route.query.source,
    },
    server: false
})

console.log(data.value)

</script>