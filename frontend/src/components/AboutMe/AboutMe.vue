<template>
    <div>
        <p class="text-2xl font-bold cursor-pointer" @click="openModal">
            ABOUT ME
        </p>
        <div
            class="ml-4"
        >
            <div class="mt-2 relative rounded-md">
            <p class="block w-full text-sm" contenteditable="true" placeholder="Detail">{{}}</p>            
            </div>
        </div>
    </div>
</template>