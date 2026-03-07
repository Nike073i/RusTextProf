import { src, dest } from "gulp";
import plumber from "gulp-plumber";
import flatten from "gulp-flatten";
import rigger from "gulp-rigger";
import uglify from "gulp-uglify";
import merge from "gulp-merge";
import replace from "gulp-replace"


export function configureBuildJsTask({
    mainScriptSrc,
    pageScriptsSrc,
    basePath,
    toDist,
    envs = {},
    continuePipe = pipeline => pipeline,
}) {
    const useEnvironment = (pipeline, name, value) =>
        pipeline.pipe(replace(`__${name}__`, value))

    const useEnvironments = (pipeline, envs) => Object.entries(envs).reduce((currentPipeline, [name, value]) => useEnvironment(currentPipeline, name, value), pipeline)

    function buildJs() {
        const mainScript = src(mainScriptSrc)
            .pipe(plumber())
            .pipe(rigger({
                cwd: basePath
            }));

        const pageScripts = src(`${pageScriptsSrc}/*/*.js`)
            .pipe(plumber())
            .pipe(rigger({
                cwd: basePath
            }));

        let bodyPipe = merge(mainScript, pageScripts);
        bodyPipe = useEnvironments(bodyPipe, envs);

        bodyPipe = bodyPipe
            .pipe(uglify())
            .pipe(flatten())
            .pipe(dest(toDist));

        return continuePipe(bodyPipe);
    }

    return buildJs;
}