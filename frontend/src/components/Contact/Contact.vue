<template>
    <div>
    <p class="text-2xl font-bold cursor-pointer" @click="openModal">
        CONTACT
    </p>
    <div
        class="ml-4"
    >
        <div class="mt-2 relative rounded-md">
        <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
            <span class="text-black text-base material-icons">
            cake
            </span>
        </div>
        <p class="block w-full pl-7 text-base" contenteditable="true" placeholder="mm/dd/yyyy">{{contact.birthday}}</p>
        </div>
    </div>
    <div
        class="ml-4"
    >
        <div class="mt-2 relative rounded-md">
        <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
            <span class="text-black text-base material-icons">
            email
            </span>
        </div>
        <p class="block w-full pl-7 text-base" contenteditable="true" placeholder="abc@gmail.com">{{contact.email}}</p>
        </div>
    </div>
    <div
        class="ml-4"
    >
        <div class="mt-2 relative rounded-md">
        <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
            <span class="text-black text-base material-icons">
            place
            </span>
        </div>
        <p class="block w-full pl-7 text-base" contenteditable="true" placeholder="address">{{contact.address}}</p>
        </div>
    </div>
    <div
        class="ml-4"
    >
        <div class="mt-2 relative rounded-md">
        <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
            <span class="text-black text-base material-icons">
            call
            </span>
        </div>
        <p class="block w-full pl-7 text-base" placeholder="0123456789" contenteditable="true">{{contact.phone}}</p>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            contact: {
                birthday: "12/12/2012",
                email: "trung@gmail.com",
                address: "Nhà bè",
                phone: "123456"
            },
        }
    },
}
</script>