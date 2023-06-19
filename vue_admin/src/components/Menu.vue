<template>
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-body-tertiary sidebar collapse">
        <div class="position-sticky pt-3 sidebar-sticky">
            <ul class="nav flex-column">
                <li class="nav-item">
                    <router-link to="/users" class="nav-link" active-class="active">
                        <span data-feather="home" class="align-text-bottom"></span>
                        Users
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/products" class="nav-link" active-class="active">
                        <span data-feather="home" class="align-text-bottom"></span>
                        Products
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/orders" class="nav-link" active-class="active">
                        <span data-feather="home" class="align-text-bottom"></span>
                        Orders
                    </router-link>
                </li>
            </ul>
        </div>
    </nav>
</template>
