const c = [
	() => import("..\\..\\src\\routes\\__layout.svelte"),
	() => import("..\\..\\src\\routes\\__error.svelte"),
	() => import("..\\..\\src\\routes\\index.svelte"),
	() => import("..\\..\\src\\routes\\search copy.svelte"),
	() => import("..\\..\\src\\routes\\aboutUs.svelte"),
	() => import("..\\..\\src\\routes\\brands.svelte"),
	() => import("..\\..\\src\\routes\\search.svelte")
];

const d = decodeURIComponent;

export const routes = [
	// src/routes/index.svelte
	[/^\/$/, [c[0], c[2]], [c[1]]],

	// src/routes/search copy.svelte
	[/^\/search copy\/?$/, [c[0], c[3]], [c[1]]],

	// src/routes/aboutUs.svelte
	[/^\/aboutUs\/?$/, [c[0], c[4]], [c[1]]],

	// src/routes/brands.svelte
	[/^\/brands\/?$/, [c[0], c[5]], [c[1]]],

	// src/routes/search.svelte
	[/^\/search\/?$/, [c[0], c[6]], [c[1]]]
];

// we import the root layout/error components eagerly, so that
// connectivity errors after initialisation don't nuke the app
export const fallback = [c[0](), c[1]()];