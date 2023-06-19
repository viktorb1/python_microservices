<template>
  <div>
    <div class="container">
      <main>
        <div class="py-5 text-center">
          <h2>Welcome</h2>
          <p class="lead">{{ user.first_name }} {{ user.last_name }} has invited you to buy these products</p>
        </div>

        <div class="row g-5">
          <div class="col-md-5 col-lg-4 order-md-last">
            <h4 class="d-flex justify-content-between align-items-center mb-3">
              <span class="text-primary">Products</span>
            </h4>
            <ul class="list-group mb-3">
              <template v-for="product in products" :key="product.id">
                <li class="list-group-item d-flex justify-content-between lh-sm">
                  <div>
                    <h6 class="my-0">{{ product.title }}</h6>
                    <small class="text-body-secondary">{{ product.description }}</small>
                  </div>
                  <span class="text-body-secondary">${{ product.price }}</span>
                </li>
                <li class="list-group-item d-flex justify-content-between lh-sm">
                  <div>
                    <h6 class="my-0">Quantity</h6>
                  </div>
                  <input v-model="quantities[product.id]" class="text-muted form-control quantity" type="number"
                    min="0" />
                </li>
              </template>


              <li class="list-group-item d-flex justify-content-between">
                <span>Total (USD)</span>
                <strong>${{ total }}</strong>
              </li>
            </ul>

          </div>
          <div class="col-md-7 col-lg-8">
            <h4 class="mb-3">Personal info</h4>
            <form class="needs-validation" @submit.prevent="submit">
              <div class="row g-3">
                <div class="col-sm-6">
                  <label for="firstName" class="form-label">First name</label>
                  <input v-model="inputFields.first_name" type="text" class="form-control" id="firstName"
                    placeholder="First Name" required>
                </div>

                <div class="col-sm-6">
                  <label for="lastName" class="form-label">Last name</label>
                  <input v-model="inputFields.last_name" type="text" class="form-control" id="lastName"
                    placeholder="Last Name" required>
                </div>


                <div class="col-12">
                  <label for="email" class="form-label">Email</label>
                  <input v-model="inputFields.email" type="email" class="form-control" id="email"
                    placeholder="you@example.com">
                </div>

                <div class="col-12">
                  <label for="address" class="form-label">Address</label>
                  <input v-model="inputFields.address" type="text" class="form-control" id="address"
                    placeholder="1234 Main St" required>
                </div>

                <div class="col-md-5">
                  <label for="country" class="form-label">Country</label>
                  <input v-model="inputFields.country" type="text" class="form-control" id="country"
                    placeholder="Country">
                </div>

                <div class="col-md-4">
                  <label for="city" class="form-label">City</label>
                  <input v-model="inputFields.city" type="text" class="form-control" id="city" placeholder="City">
                </div>

                <div class="col-md-3">
                  <label for="zip" class="form-label">Zip</label>
                  <input v-model="inputFields.zip" type="text" class="form-control" id="zip" placeholder="Zip">
                </div>
              </div>
              <hr class="my-4">
              <button class="w-100 btn btn-primary btn-lg" type="submit">Checkout</button>
            </form>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { loadStripe } from '@stripe/stripe-js'


const user = ref({})
const products = ref([])
const quantities = ref({})
const inputFields = reactive({
  first_name: "",
  last_name: "",
  email: "",
  address: "",
  country: "",
  city: "",
  zip: ""
})

const route = useRoute()

const { data } = await useAPIFetch(`links/${route.params.code}`)
user.value = data.value.user
products.value = data.value.products

products.value.forEach(p => {
  quantities.value[p.id] = 0;
})

const total = computed(() => {
  return products.value.reduce((s, p) => {
    return s + (p.price * quantities.value[p.id])
  }, 0)
})

const submit = async () => {
  const body = {
    ...inputFields,
    code: route.params.code,
    products: products.value.map(p => ({
      product_id: p.id,
      quantity: quantities.value[p.id]
    }))
  }

  const { data } = await useAPIFetch("orders", { method: 'POST', body: body })
  const config = useRuntimeConfig()
  const stripe = await loadStripe(config.public.stripePk)
  console.log(data.value)

  const { error } = await stripe.redirectToCheckout({
    sessionId: data.value.id
  })
}
</script>

<style scoped>
.quantity {
  width: 65px;
}
</style>