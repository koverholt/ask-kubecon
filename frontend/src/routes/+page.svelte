<script lang="ts">
	import { Navbar, NavBrand, NavLi, NavUl } from 'flowbite-svelte';
	import { Heading, A, Label, Card } from 'flowbite-svelte';
	import { Section, Cta } from 'flowbite-svelte-blocks';
	import { Alert } from 'flowbite-svelte';
	import { InfoCircleSolid } from 'flowbite-svelte-icons';
	import { ButtonGroup, Button } from 'flowbite-svelte';
</script>

<Navbar class="bg-[#615D98] pt-2">
	<NavBrand>
		<span class="self-center whitespace-nowrap text-xl font-semibold text-[#e4fef6]">
			Ask KubeCon
		</span>
	</NavBrand>
	<NavUl>
     <NavLi class="text-gray-50"
     href="https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/">KubeCon
     Website</NavLi>
		<NavLi
			class="text-gray-50"
			href="https://cloud.google.com/generative-ai-app-builder/docs/introduction"
			>Vertex AI Search</NavLi
		>
		<NavLi class="text-gray-50" href="https://cloud.google.com/ai/generative-ai"
			>Generative AI on Google Cloud</NavLi
		>
		<NavLi class="text-gray-50" href="https://github.com/koverholt/ask-kubecon">Source Code</NavLi>
	</NavUl>
</Navbar>

<div class="flex flex-col w-full px-10">
	<!-- <div class="mt-10 px-10 -mb-20">
		<img src="dora.png" width="400px" alt="DevOps Research and Assessment (DORA)" />
	</div> -->
	<Section name="cta">
		<Cta ctatype="image">
			<svelte:fragment slot="h2">Ask KubeCon anything in natural language</svelte:fragment>
			<p class="mt-6 mb-2 font-light text-gray-500 dark:text-gray-400 md:text-lg">
				This app uses
				<A
					href="https://cloud.google.com/generative-ai-app-builder/docs/introduction"
					class="font-medium hover:underline break-normal text-[#0000EE]">Vertex AI Search</A
				> and generative AI functionality in <A
					class="font-medium
        hover:underline break-normal text-[#0000EE]"
					href="https://cloud.google.com/">Google Cloud</A
				> to search and summarize content on the <A
					class="font-medium hover:underline break-normal text-[#0000EE]"
					href="https://dora.dev/">DORA website</A
				> using LLMs and a conversational search experience.
			</p>
		</Cta>

		<form class="w-full flex flex-col items-center -mt-6" on:submit|preventDefault={onSubmit}>
			<h1 class="my-2 text-white text-xl text-center">My custom search widget</h1>
			<!-- <div class="text-center mb-8">
				<span class="font-bold">Example questions:</span>
				<ButtonGroup>
					<Button on:click={() => updateSearchField('What are the Four Key Metrics?')}>
						What are the Four Key Metrics?</Button
					>
					<Button on:click={() => updateSearchField('How can I measure developer happiness?')}>
						How can I measure developer happiness?
					</Button>
					<Button
						on:click={() => updateSearchField('What are the benefits of having strong user focus?')}
					>
						What are the benefits of having strong user focus?
					</Button>
				</ButtonGroup>
			</div> -->
			<div>
				<div class="relative text-gray-600 focus-within:text-gray-400 flex justify-center gap-2">
					<span class="absolute inset-y-0 left-0 flex items-center pl-2">
						<button type="submit" class="p-1 focus:outline-none focus:shadow-outline">
							<svg
								fill="none"
								stroke="currentColor"
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								viewBox="0 0 24 24"
								class="w-6 h-6"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg
							>
						</button>
					</span>
					<input
						type="search"
						name="search"
						id="searchWidgetTrigger"
						class="py-2 text-md w-[500px] text-black bg-white rounded-md pl-10 focus:bg-white focus:text-gray-900"
						placeholder="Ask KubeCon anything..."
					/>
					<!-- <button
						id="submit"
						type="submit"
						disabled={!ready || waiting}
						class="bg-blue-500 w-[100px] h-[40px] hover:bg-blue-700 disabled:bg-slate-900 text-white font-bold py-2 px-4 rounded flex justify-center"
					>
						{#if waiting}
							<svg
								class="animate-spin mt-[0.1rem] h-5 w-5 text-white"
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
							>
								<circle
									class="opacity-25"
									cx="12"
									cy="12"
									r="10"
									stroke="currentColor"
									stroke-width="4"
								/>
								<path
									class="opacity-75"
									fill="currentColor"
									d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
								/>
							</svg>
						{:else}
							Search
						{/if}
					</button>
					<button
						id="clear"
						type="reset"
						class="bg-gray-500 w-[100px] h-[40px] hover:bg-blue-700 disabled:bg-slate-900 text-white font-bold py-2 px-4 rounded flex justify-center"
						on:click={resetForm}
						>Reset
					</button> -->
				</div>
			</div>
		</form>

		<!-- Widget JavaScript bundle -->
		<script src="https://cloud.google.com/ai/gen-app-builder/client?hl=en_US"></script>

		<!-- Search widget element is not visible by default -->
		<gen-search-widget
			configId="f50071d6-9856-4e98-8204-0c7fc61acd3c"
			triggerId="searchWidgetTrigger">
		</gen-search-widget>

		<!-- Element that opens the widget on click. It does not have to be an input -->
		<!-- <input placeholder="Search here" id="searchWidgetTrigger" /> -->
	</Section>

</div>
