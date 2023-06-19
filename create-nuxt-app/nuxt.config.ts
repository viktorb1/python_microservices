// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    port: 3001,
  },
  css: ["bootstrap/dist/css/bootstrap.css"],
  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL,
      stripePk: process.env.STRIPE_PK,
    },
  },
});
