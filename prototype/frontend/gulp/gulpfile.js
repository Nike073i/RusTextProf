import { deleteAsync } from "del";
import { series, watch, parallel } from "gulp";
import { configureCreateDocsTask } from "./docs.js";
import { configureCopyExamplesTask } from "./examples.js";
import { configureCopyMediaTask } from "./media.js";
import { configureBuildHtmlTask } from "./html.js";
import { configureBuildCssTask } from "./scss.js";
import { configureBuildJsTask } from "./js.js";
import { modifyStream, configureDevServerTask } from "./browsersync.js"

const paniniOptions = {
    root: "../src/pages/*/",
    layouts: "../src/shared/layouts/",
    partials: ["../src/shared/partials/**/", "../src/pages/*/partials/"],
    data: ["../src/data/", "../src/pages/*/data/"]
};

const createDocsTask = configureCreateDocsTask({
    fromSrc: "../content/docs",
    toDist: "../dist/info",
    paniniOptions
})

const copyExamplesTask = configureCopyExamplesTask({
    fromSrc: "../content/examples",
    toDist: "../dist/examples",
})

const copyMediaTask = configureCopyMediaTask({
    mediaOptions: [
        {
            fromSrc: "../src/assets/icons",
            toDist: "../dist/icons"
        },
        {
            fromSrc: "../src/assets/images",
            toDist: "../dist/images"
        },
    ]
})

const buildHtml = configureBuildHtmlTask({
    fromSrc: "../src/pages",
    toDist: "../dist",
    paniniOptions,
    continuePipe: pipeline => pipeline.pipe(modifyStream())
})

const buildCss = configureBuildCssTask({
    mainStyleSrc: "../src/shared/styles/style.scss",
    pageStylesSrc: "../src/pages",
    toDist: "../dist/css",
    continuePipe: pipeline => pipeline.pipe(modifyStream())
})

const buildJs = configureBuildJsTask({
    mainScriptSrc: '../src/shared/scripts/site.js',
    pageScriptsSrc: "../src/pages",
    basePath: "../src",
    toDist: "../dist/js",
    envs: {
        BACKEND_URL: process.env.BACKEND_URL || 'http://localhost:8000',
    },
    continuePipe: pipeline => pipeline.pipe(modifyStream())
})

const serve = configureDevServerTask({
    baseDir: "../dist",
})


function watchFiles() {
    watch(["../src/**/*.html"], buildHtml);
    watch(["../src/**/*.js"], buildJs);
    watch(["../src/**/*.scss"], buildCss);
    watch(["../src/**/*.{svg, png, jpg, jpeg, gif}"], copyMediaTask);
    watch(["../content/**/*.{md, jpg,jpeg,png,gif,svg,bmp,ico,mp4,webm,ogg}"], createDocsTask);
}

function clean() {
    return deleteAsync("../dist/", { force: true });
}

const build = series(clean, parallel(buildHtml, buildCss, buildJs, copyMediaTask, createDocsTask, copyExamplesTask));
const devServer = series(build, parallel(serve, watchFiles));

export default build;
export {
    build,
    devServer,
    clean,
    createDocsTask,
    copyExamplesTask,
}