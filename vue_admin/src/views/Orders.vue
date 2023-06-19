<template>
    <div>
        <v-expansion-panels>
            <v-expansion-panel v-for="order in orders" :key="order.id">
                <v-expansion-panel-title>
                    {{ `${order.first_name} ${order.last_name}, $${order.total}` }}
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-table>
                        <template v-slot:default>
                            <thead>
                                <tr>
                                    <th class="text-left">#</th>
                                    <th class="text-left">Product Title</th>
                                    <th class="text-left">Price</th>
                                    <th class="text-left">Quantity</th>
                                </tr>
                            </thead>



                            <tbody>
                                <tr v-for="item in order.order_items" :key="order.id">
                                    <td>{{ item.id }}</td>
                                    <td>{{ item.product_title }}</td>
                                    <td>$ {{ item.price }}</td>
                                    <td>{{ item.quantity }}</td>
                                </tr>
                            </tbody>
                        </template>
                    </v-table>
                </v-expansion-panel-text>
            </v-expansion-panel>
        </v-expansion-panels>
        <!-- <v-pagination v-model="page" total-visible="7" :length="last_page"></v-pagination> -->
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue"
import axios from "axios"

let orders = ref([])

onMounted(async () => {
    const { data } = await axios.get('orders', { withCredentials: true })
    orders.value = data
})
</script>


<style scoped></style>
