"""
add glsl shaders to your kivy widget
====================================

this ae namespace portion provides the mixin class :class:`ShadersMixin` that can be combined with any Kivy widget to
display GLSL-/shader-based graphics, gradients and animations.

additionally some :ref:`built-in shaders` are integrated into this portion. more shader examples can be found in the
glsl sub-folder of the `GlslTester <https://github.com/AndiEcker/glsl_tester>`_ demo application.


usage of ShadersMixin class
---------------------------

to add the :class:`ShadersMixin` mixin class to a Kivy widget in your python code file you have to specify it in the
declaration of your widget class. the following example is extending Kivy's :class:`~kivy.uix.boxlayout.BoxLayout`
layout with a shader::

    from kivy.uix.boxlayout import BoxLayout
    from ae.kivy_glsl import ShadersMixin

    class MyBoxLayoutWithShader(ShadersMixin, BoxLayout):


alternatively you can declare a your shader-widget as a new kv rule within a kv file::

    <MyBoxLayoutWithShader@ShadersMixin+BoxLayout>


to register a shader, call the :meth:`ShadersMixin.add_shader` method::

    shader_id = widget_instance.add_shader()


by default :meth:`~ShadersMixin.add_shader` is using the built-in
:data:`plasma hearts shader <PLASMA_HEARTS_SHADER_CODE>`, provided by this portion. the next example is instead using
the built-in :data:`plunge waves shader <PLUNGE_WAVES_SHADER_CODE>`::

    from ae.kivy_glsl import BUILT_IN_SHADERS

    widget_instance.add_shader(shader_code=BUILT_IN_SHADERS['plunge_waves'])


alternatively you can use your own shader code by specifying it on call of the method :meth:`~ShadersMixin.add_shader`
either as code block string to the `paramref:`~ShadersMixin.add_shader.shader_code` argument or as file name to the
`paramref:`~ShadersMixin.add_shader.shader_file` argument.

animation shaders like the built-in plunge waves and plasma hearts shaders need to be refreshed by a timer. the
refreshing frequency can be specified via the :paramref:`~ShadersMixin.add_shader.update_freq` parameter. to disable the
automatic creation of a timer event pass a zero value to this argument.

.. hint::
    the demo apps `ComPartY <https://gitlab.com/ae-group/comparty>`_ and
    `GlslTester <https://github.com/AndiEcker/glsl_tester>`_ are disabling the automatic timer event
    for each shader and using instead a Kivy clock timer to update the frames of all active shaders.


store the return value of :meth:`~ShadersMixin.add_shader` to stop, pause or to delete the shader later. the following
examples demonstrates the deletion of a shader by calling the :meth:`~ShadersMixin.del_shader` method::

    widget_instance.del_shader(shader_id)


.. note::
    you can activate multiple shaders for the same widget. the visibility and intensity of each shader depends then on
    the implementation of the shader codes and the values of the input arguments (especially `alpha` and `tex_col_mix`)
    for each shader (see parameter :paramref:`~ShadersMixin.add_shader.glsl_dyn_args`).


shader compilation errors and renderer crashes
----------------------------------------------

on some devices (mostly on Android) the shader script does not compile. the success property of Kivy's shader class
is then set to False and an error message like the following gets printed on to the console output::

    [ERROR  ] [Shader      ] <fragment> failed to compile (gl:0)
    [INFO   ] [Shader      ] fragment shader: <b"0:27(6): error: ....

some common failure reasons are:

    * missing declaration of used uniform input variables.
    * non-input/output variables declared on module level (they should be moved into main or any other function).

if a compile error occurred then the `run_state` value of the shader id dict will be set to `'error'` - check the value
of the `error_message` key of the shader id dict for more details on the error.

in other cases the shader code compiles fine but then the renderer is crashing in the vbo.so library and w/o
printing any Python traceback to the console - see also `this Kivy issues <https://github.com/kivy/kivy/issues/6627>`_).

if the crash only happens on some Adreno GPUs then see issues `https://github.com/kivy/python-for-android/issues/2723`_
and `https://github.com/kivy/kivy/issues/8080`_ and a possible fix in `https://github.com/kivy/kivy/pull/8098`_.
sometimes these type of crashes can be prevented if the texture of the widget (or of the last shader) gets fetched
(w/ the function texture2D(texture0, tex_coord0)) - even if it is not used for the final gl_FragColor output variable.
in some cases additional to fetch the texture, the return value of the `texture2D` call has to be accessed at least once
at the first render cycle.


built-in shaders
----------------

the :data:`circled alpha shader <CIRCLED_ALPHA_SHADER_CODE>` is a simple gradient pixel shader without any time-based
animations.

the :data:`plunge waves shader <PLUNGE_WAVES_SHADER_CODE>` is animated and inspired by the kivy pulse shader example
(Danguafer/Silexars, 2010) https://github.com/kivy/kivy/blob/master/examples/shader/shadertree.py.

the animated :data:`plasma hearts shader <PLASMA_HEARTS_SHADER_CODE>` is inspired by the kivy plasma shader example
https://github.com/kivy/kivy/blob/master/examples/shader/plasma.py.

.. hint::
    the `GlslTester <https://github.com/AndiEcker/glsl_tester>`_ and `ComPartY <https://gitlab.com/ae-group/comparty>`_
    applications are demonstrating the usage of this portion.

the literals of the built-in shaders got converted into constants, following the recommendations given in the accepted
answer of `this SO question <https://stackoverflow.com/questions/20936086>`_.
"""
import re
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from kivy.clock import Clock                                    # type: ignore
from kivy.factory import Factory                                # type: ignore
from kivy.graphics.instructions import RenderContext            # type: ignore # pylint: disable=no-name-in-module
from kivy.graphics.vertex_instructions import (                 # type: ignore # pylint: disable=no-name-in-module
    Ellipse, Rectangle, RoundedRectangle)
from kivy.properties import ListProperty                        # type: ignore # pylint: disable=no-name-in-module

from ae.base import UNSET                                       # type: ignore


__version__ = '0.3.14'


DEFAULT_FPS = 30.0                                              #: default frames-per-second

ShaderIdType = Dict[str, Any]                                   #: shader internal data and id

# --- BUILT-IN SHADERS

CIRCLED_ALPHA_SHADER_CODE = '''\
uniform float alpha;
uniform float tex_col_mix;
uniform vec2 center_pos;
uniform vec2 win_pos;
uniform vec2 resolution;
uniform vec4 tint_ink;

void main(void)
{
  vec2 pix_pos = (frag_modelview_mat * gl_FragCoord).xy;
  float len = length(pix_pos - center_pos);
  pix_pos -= win_pos;
  float dis = len / max(pix_pos.x, max(pix_pos.y, max(resolution.x - pix_pos.x, resolution.y - pix_pos.y)));
  vec3 col = tint_ink.rgb;
  if (tex_col_mix != 0.0) {
    vec4 tex = texture2D(texture0, tex_coord0);
    col = mix(tex.rgb, col, tex_col_mix);
  }
  gl_FragColor = vec4(col, dis * alpha);
}
'''

PLASMA_HEARTS_SHADER_CODE = '''\
uniform float alpha;
uniform float contrast;
uniform float tex_col_mix;
uniform float time;
uniform vec2 center_pos;
uniform vec2 win_pos;
uniform vec2 resolution;
uniform vec4 tint_ink;

const float THOUSAND = 963.9;
const float HUNDRED = 69.3;
const float TEN = 9.9;
const float TWO = 1.83;
const float ONE = 0.99;

void main(void)
{
  vec2 pix_pos = (frag_modelview_mat * gl_FragCoord).xy - win_pos;
  vec2 rel_center = center_pos - win_pos;
  float x = abs(pix_pos.x - rel_center.x);
  float y = abs(pix_pos.y - rel_center.y - resolution.y);

  float m1 = x + y + cos(sin(time) * TWO) * HUNDRED + sin(x / HUNDRED) * THOUSAND;
  float m2 = y / resolution.y;
  float m3 = x / resolution.x + time * TWO;

  float c1 = abs(sin(m2 + time) / TWO + cos(m3 / TWO - m2 - m3 + time));
  float c2 = abs(sin(c1 + sin(m1 / THOUSAND + time) + sin(y / HUNDRED + time) + sin((x + y) / HUNDRED) * TWO));
  float c3 = abs(sin(c2 + cos(m2 + m3 + c2) + cos(m3) + sin(x / THOUSAND)));

  vec4 tex = texture2D(texture0, tex_coord0);
  float dis = TWO * distance(pix_pos, rel_center) / max(resolution.x, resolution.y);
  vec4 col = vec4(c1, c2, c3, contrast * (ONE - dis)) * tint_ink * TWO;
  col = mix(tex, col, tex_col_mix);
  gl_FragColor = vec4(col.rgb, col.a * sqrt(alpha));
}
'''

COLORED_SMOKE_SHADER_CODE = '''\
uniform float alpha;
uniform float tex_col_mix;
uniform float time;
uniform vec2 center_pos;
uniform vec2 mouse;         // density, speed
uniform vec2 resolution;
uniform vec4 tint_ink;

const float ONE = 0.99999999999999;

float rand(vec2 n) {
 //This is just a compounded expression to simulate a random number based on a seed given as n
 return fract(cos(dot(n, vec2(12.98982, 4.14141))) * 43758.54531);
}

float noise(vec2 n) {
 //Uses the rand function to generate noise
 const vec2 d = vec2(0.0, ONE);
 vec2 b = floor(n), f = smoothstep(vec2(0.0), vec2(ONE), fract(n));
 return mix(mix(rand(b), rand(b + d.yx), f.x), mix(rand(b + d.xy), rand(b + d.yy), f.x), f.y);
}

float fbm(vec2 n) {
 //fbm stands for "Fractal Brownian Motion" https://en.wikipedia.org/wiki/Fractional_Brownian_motion
 float total = 0.0;
 float amplitude = 1.62;
 for (int i = 0; i < 3; i++) {
  total += noise(n) * amplitude;
  n += n;
  amplitude *= 0.51;
 }
 return total;
}

void main() {
 //This is where our shader comes together
 const vec3 c1 = vec3(126.0/255.0, 0.0/255.0, 96.9/255.0);
 //const vec3 c2 = vec3(173.0/255.0, 0.0/255.0, 161.4/255.0);
 vec3 c2 = tint_ink.rgb;
 const vec3 c3 = vec3(0.21, 0.0, 0.0);
 const vec3 c4 = vec3(165.0/255.0, 129.0/255.0, 214.4/255.0);
 const vec3 c5 = vec3(0.12);
 const vec3 c6 = vec3(0.9);
 vec2 pix_pos = (gl_FragCoord.xy - center_pos) / resolution.xy - vec2(0.0, 0.51);
 //this is how "packed" the smoke is in our area. try changing 15.0 to 2.1, or something else
 vec2 p = pix_pos * (ONE + mouse.x / resolution.x * 15.0);
 //the fbm function takes p as its seed (so each pixel looks different) and time (so it shifts over time)
 float q = fbm(p - time * 0.12);
 float speed = 3.9 * time * mouse.y / resolution.y;
 vec2 r = vec2(fbm(p + q + speed - p.x - p.y), fbm(p + q - speed));
 vec3 col = (mix(c1, c2, fbm(p + r)) + mix(c3, c4, r.y) - mix(c5, c6, r.x)) * cos(pix_pos.y);
 col *= ONE - pix_pos.y;
 if (tex_col_mix != 0.0) {
  vec4 tex = texture2D(texture0, tex_coord0);
  col = mix(tex.rgb, col, tex_col_mix);
 }
 gl_FragColor = vec4(col, (alpha + tint_ink.a) / 2.01);
}
'''

FIRE_STORM_SHADER_CODE = '''\
uniform float alpha;
uniform float contrast;  // speed
uniform float tex_col_mix;
uniform float time;
uniform vec2 center_pos;
uniform vec2 mouse;  // intensity, granularity
uniform vec2 resolution;
uniform vec4 tint_ink;

#define TAU 6.283185307182
#define MAX_ITER 15

void main( void ) {
 float t = time*contrast + 23.01;
 // uv should be the 0-1 uv of texture...
 vec2 xy = (gl_FragCoord.xy - center_pos) / resolution.yy; // - vec2(0.9);
 vec2 uv = vec2(atan(xy.y, xy.x) * 6.99999 / TAU, log(length(xy)) * (0.21 + mouse.y / resolution.y) - time * 0.21);
 vec2 p = mod(uv*TAU, TAU)-250.02;
 vec2 i = vec2(p);
 float c = 8.52;
 float intensity = 0.003 + mouse.x / resolution.x / 333.3;  // = .005;

 for (int n = 0; n < MAX_ITER; n++) {
   float t = t * (1.02 - (3.498 / float(n+1)));
   i = p + vec2(cos(t - i.x) + sin(t + i.y), sin(t - i.y) + cos(t + i.x));
   c += 1.0/length(vec2(p.x / (sin(i.x+t)/intensity),p.y / (cos(i.y+t)/intensity)));
 }
 c /= float(MAX_ITER);
 c = 1.272 - pow(c, 6.42);
 vec3 colour = vec3(pow(abs(c), 8.01));
 colour = clamp(colour + tint_ink.rgb, 0.0, 0.999999);
 if (tex_col_mix != 0.0) {
  vec4 tex = texture2D(texture0, tex_coord0);
  colour = mix(tex.rgb, colour, tex_col_mix);
 }
 gl_FragColor = vec4(colour, (alpha + tint_ink.a) / 2.00001);
 }
'''

PLUNGE_WAVES_SHADER_CODE = '''\
uniform float alpha;
uniform float contrast;
uniform float tex_col_mix;
uniform float time;
uniform vec2 center_pos;
uniform vec2 win_pos;
uniform vec2 resolution;
uniform vec4 tint_ink;

const float TEN = 9.99999;
const float TWO = 2.00001;
const float ONE = 0.99999;

void main(void)
{
  vec2 pix_pos = (frag_modelview_mat * gl_FragCoord).xy;
  float len = length(pix_pos - center_pos);
  float col_comp = (sin(len / TEN - mod(time, TEN) * TEN) + ONE) / TEN;
  float dis = len / (TWO * min(resolution.x, resolution.y));
  vec4 col = tint_ink / vec4(col_comp, col_comp, col_comp, dis / (ONE / TEN + contrast)) / TEN;
  if (tex_col_mix != 0.0) {
    vec4 tex = texture2D(texture0, tex_coord0);
    col = mix(tex, col, tex_col_mix);
  }
  gl_FragColor = vec4(col.rgb, col.a * alpha * alpha);
}
'''

WORM_WHOLE_SHADER_CODE = '''\
uniform float alpha;
uniform float contrast;
uniform float tex_col_mix;
uniform float time;
uniform vec2 center_pos;
uniform vec2 mouse;         // off1, off2
uniform vec2 resolution;
uniform vec4 tint_ink;

const float XIS = 0.6;
const float ONE = 0.99999999999;
const float TWO = 1.99999999998;
const float SIX = 6.0;

void main(void){
 vec2 centered_coord = (TWO * (gl_FragCoord.xy - center_pos) - resolution) / resolution.y;
 centered_coord += vec2(resolution.x / resolution.y, ONE);
 centered_coord.y *= dot(centered_coord, centered_coord);
 float dist_from_center = length(centered_coord);
 float dist_from_center_y = length(centered_coord.y);
 float u = SIX / dist_from_center_y + time * SIX;
 float v = (SIX / dist_from_center_y) * centered_coord.x;
 float grid = (ONE - pow(sin(u) + ONE, XIS) + (ONE - pow(sin(v) + ONE, XIS))) * dist_from_center_y * contrast * 6000.0;
 float off1 = sin((fract(time / SIX) + dist_from_center) * SIX) * (XIS + mouse.x / resolution.x);
 float off2 = sin((fract(time / SIX) + dist_from_center_y * TWO) * SIX) * (XIS + mouse.y / resolution.y);
 vec3 col = vec3(grid) * vec3(tint_ink.r * off1, tint_ink.g * off1 * off2 * TWO, tint_ink.b * off2);
 if (tex_col_mix != 0.0) {
  vec4 tex = texture2D(texture0, tex_coord0);
  col = mix(tex.rgb, col, tex_col_mix);
 }
 gl_FragColor=vec4(col, alpha);
}
'''

BUILT_IN_SHADERS = dict(
    circled_alpha=CIRCLED_ALPHA_SHADER_CODE, colored_smoke=COLORED_SMOKE_SHADER_CODE, fire_storm=FIRE_STORM_SHADER_CODE,
    plasma_hearts=PLASMA_HEARTS_SHADER_CODE, plunge_waves=PLUNGE_WAVES_SHADER_CODE, worm_whole=WORM_WHOLE_SHADER_CODE)
""" dict of built-in shader code blocks - key specifies shader in :paramref:`~ShadersMixin.add_shader.shader_code`. """

RENDER_SHAPES = (Ellipse, Rectangle, RoundedRectangle)
""" supported render shapes, specified in :paramref:`~ShadersMixin.add_shader.render_shape`. """


SHADER_PARAMETER_MATCHER = re.compile(r"^uniform (float|vec2|vec4) ([a-z_]+);", re.M)  #: match uniform var declarations
HIDDEN_SHADER_PARAMETERS = ('resolution', 'time', 'win_pos')   #: uniform vars that are not editable by the user


def shader_parameter_alias(shader_code: str, arg_name: str) -> str:
    """ check for alias for the passed shader argument name in the passed shader code.

    :param shader_code:     shader code to determine the parameter alias names (from comment of uniform declaration).
    :param arg_name:        shader arg name.
    :return:                alias (if found) or shader arg name (if not).
    """
    idx = shader_code.find(" " + arg_name + ";")
    if idx >= 0:
        line = shader_code[idx + len(arg_name) + 2:shader_code.find("\n", idx)]
        idx = line.find("// ")
        if idx >= 0:
            arg_name = line[idx + 3:]
    return arg_name


def shader_parameters(shader_code: str) -> Tuple[str, ...]:
    """ shader arg names of the shader code in the passed shader code.

    :param shader_code:     shader code from which to determine the declared uniform parameter names.
    :return:                tuple of shader arg names of the shader code passed into the argument
                            :paramref:`~shader_parameters.shader_code`, plus the `start_time` argument which controls,
                            independent from to be included in the shader code, how the `time` argument get prepared in
                            each render frame (see also :paramref:`~ae.kivy_glsl.ShadersMixin.add_shader.start_time`).
    """
    return ('start_time', ) + tuple(nam for typ, nam in re.findall(SHADER_PARAMETER_MATCHER, shader_code)
                                    if nam not in HIDDEN_SHADER_PARAMETERS)


class ShadersMixin:
    """ shader mixin base class """
    # abstract attributes provided by the Widget instance mixed into
    canvas: Any
    center_x: float
    center_y: float
    fbind: Callable
    parent: Any
    pos: list
    size: list
    to_window: Callable
    unbind_uid: Callable

    # attributes
    added_shaders = ListProperty()                  #: list of shader-ids/kwarg-dicts for each shader
    running_shaders: List[ShaderIdType] = []        #: list/pool of active/running shaders/render-contexts

    _pos_fbind_uid: int = 0
    _size_fbind_uid: int = 0

    def add_shader(self, add_to: str = '',
                   shader_code: str = PLASMA_HEARTS_SHADER_CODE, shader_file: str = "",
                   start_time: Optional[float] = 0.0, update_freq: float = DEFAULT_FPS,
                   run_state: str = 'running', render_shape: Union[Any, str] = Rectangle,
                   **glsl_dyn_args) -> ShaderIdType:
        """ add/register a new shader for the mixing-in widget.

        :param add_to:          '' to add to current canvas, 'before' and 'after' to the before/after canvas of
                                the widget instance mixed-into. if the canvas does not exist then the shaders
                                render context will be set as a current canvas.
        :param shader_code:     fragment shader code block or key of BUILT_IN_SHADERS dict if first character is '='.
                                this argument will be ignored if :paramref:`~add_shader.shader_file` is not empty.
        :param shader_file:     filename with the glsl shader code (with “–VERTEX” or “–FRAGMENT” sections) to load.
        :param start_time:      base/start time. passing the default value zero is syncing the `time` glsl parameter of
                                of this shader with :meth:`kivy.clock.Clock.get_boottime()`. pass ``None`` to initialize
                                this argument to the current Clock boot time, to start the `time` glsl argument at zero.
        :param update_freq:     shader render update frequency. pass 0.0 to disable creation of an update timer.
        :param run_state:       optional shader run state (default='running'), pass 'paused'/'error' to not run it.
        :param render_shape:    pass one of the supported shapes (:data:`RENDER_SHAPES`) either as shape class or str.
        :param glsl_dyn_args:   extra/user dynamic shader parameters, depending on the used shader code. the keys
                                of this dict are the names of the corresponding glsl input variables in your shader
                                code. the built-in shaders (provided by this module) providing the following glsl
                                input variables:

                                * `'alpha'`: opacity (float, 0.0 - 1.0).
                                * `'center_pos'`: center position in Window coordinates (tuple(float, float)).
                                * `'contrast'`: color contrast (float, 0.0 - 1.0).
                                * `'mouse'`: mouse pointer position in Window coordinates (tuple(float, float)).
                                * `'resolution'`: width and height in Window coordinates (tuple(float, float)).
                                * `'tex_col_mix'`: factor (float, 0.0 - 1.0) to mix the kivy input texture
                                   and the calculated color. a value of 1.0 will only show the shader color,
                                   whereas 0.0 will result in the color of the input texture (uniform texture0).
                                * `'tint_ink'`: tint color with color parts in the range 0.0 till 1.0.
                                * `'time'`: animation time (offset to :paramref:`~add_shader.start_time`) in seconds. if
                                   specified as constant (non-dynamic) value then you have to call the
                                   :meth:`.next_tick` method to increment the timer for this shader.

                                pass a callable to provide a dynamic/current value, which will be called on
                                each rendering frame without arguments and the return value will be passed into
                                the glsl shader.

                                .. note::
                                    don't pass `int` values because some renderer will interpret them as `0.0`.

        :return:                index (id) of the created/added render context.
        """
        if start_time is None:
            start_time = Clock.get_boottime()
        if 'center_pos' not in glsl_dyn_args:
            glsl_dyn_args['center_pos'] = lambda: (self.center_x, self.center_y)
        if 'tint_ink' not in glsl_dyn_args:
            glsl_dyn_args['tint_ink'] = [0.546, 0.546, 0.546, 1.0]  # colors * shader_code.TWO ~= [1.0, 1.0, 1.0]

        shader_id = dict(add_to=add_to, run_state=run_state, render_shape=render_shape,
                         shader_code=shader_code, shader_file=shader_file,
                         start_time=start_time, update_freq=update_freq, glsl_dyn_args=glsl_dyn_args)

        self.added_shaders.append(shader_id)    # register in ListProperty -> compile/add-to-canvas/... if running state

        return shader_id

    def _compile_shader(self, shader_id: ShaderIdType) -> RenderContext:
        """ try to compile glsl shader file/code - raise ValueError if compilation failed.

        :param shader_id:       shader id (internal data dict with either `shader_file` (preference) or
                                `shader_code` key representing the shader code to use).
        :return:                kivy/glsl render context with the compiled shader attached to it.
        """
        ren_ctx = RenderContext(use_parent_modelview=True, use_parent_projection=True,
                                use_parent_frag_modelview=True)
        with ren_ctx:
            shape = shader_id['render_shape']
            if isinstance(shape, str):
                for sha in RENDER_SHAPES:
                    if sha.__name__ == shape:
                        shape = sha
                        break
                else:
                    ValueError(f"render shape {shape} is not supported")
            shader_id['rectangle'] = shape(pos=self.pos, size=self.size)

        shader = ren_ctx.shader
        shader_file = shader_id['shader_file']
        try:
            if shader_file:
                old_value = shader.source
                shader.source = shader_file
            else:
                old_value = shader.fs
                hdr = "$HEADER$"  # Kivy header.fs file template placeholder
                shader_code = shader_id['shader_code']
                if shader_code[0] == '=':
                    shader_code = BUILT_IN_SHADERS[shader_code[1:]]
                shader.fs = ("" if hdr in shader_code else hdr) + shader_code
            fail_reason = "" if shader.success else "shader.success is False"

        except Exception as ex:
            fail_reason = f"exception {ex}"
            old_value = UNSET

        if fail_reason:
            if old_value is not UNSET:
                if shader_file:
                    shader.source = old_value
                else:
                    shader.fs = old_value
            err_msg = f"shader compilation error: '{fail_reason}' (see console output)"
            shader_id['error_message'] = err_msg
            shader_id['run_state'] = 'error'
            raise ValueError(err_msg)

        return ren_ctx

    def del_shader(self, shader_id: ShaderIdType):
        """ remove shader_id added via add_shader.

        :param shader_id:       id of the shader to remove (returned by :meth:`.add_shader`). ignoring if the passed
                                shader got already removed.
        """
        shaders = self.added_shaders
        if shader_id in shaders[:]:
            self.stop_shader(shader_id)
            shaders.remove(shader_id)

    def next_tick(self, increment: float = 1 / DEFAULT_FPS):
        """ increment glsl `time` input argument if running_shaders get updated manually/explicitly by the app.

        :param increment:       delta in seconds for the next refresh of all running_shaders with a `time` constant.
        """
        for shader_id in self.running_shaders:
            dyn_args = shader_id['glsl_dyn_args']
            if 'time' in dyn_args and not callable(dyn_args['time']):
                dyn_args['time'] += increment

    def on_added_shaders(self, *_args):
        """ added_shaders list property changed event handler. """
        self.update_shaders()

    def on_parent(self, *_args):
        """ parent changed event handler. """
        self.update_shaders()

    def play_shader(self, shader_id: ShaderIdType) -> str:
        """ create new render context canvas and add it to the widget canvas to display shader output.

        :param shader_id:       shader id and internal data dict with either `shader_file` (preference) or
                                `shader_code` key representing the shader code to use. a shader dict with the
                                `shader_code` key is a fragment shader (w/o a vertex shader), that will be automatically
                                prefixed with the Kivy fragment shader header file template, if the $HEADER$ placeholder
                                is not included in the shader code (even if it is commented out, like in the following
                                glsl code line: ``#ifdef GL_ES   //$HEADER$``).
        :return:                "" if shader is running/playing or error message string.
        """
        add_to = shader_id['add_to']
        update_freq = shader_id['update_freq']
        try:
            ren_ctx = self._compile_shader(shader_id)
            added_to = self.canvas
            if not added_to:
                self.canvas = ren_ctx
            else:
                if add_to:
                    added_to = added_to.before if add_to == 'before' else added_to.after
                added_to.add(ren_ctx)
            shader_id.update(added_to=added_to, render_ctx=ren_ctx)

            if not self.running_shaders:
                self.running_shaders = []      # create attribute on this instance (class attr untouched as emtpy list)
            self.running_shaders.append(shader_id)

            if update_freq:
                shader_id['timer'] = Clock.schedule_interval(partial(self._refresh_glsl, shader_id), 1 / update_freq)

        except (ValueError, Exception) as ex:
            err_msg = f"ShadersMixin.play_shader: shader start error - {ex}"
            shader_id['error_message'] = err_msg
            shader_id['run_state'] = 'error'
            return err_msg

        shader_id['error_message'] = ""
        shader_id['run_state'] = 'running'

        return ""

    def _pos_changed(self, *_args):
        """ pos changed event handler. """
        for shader_id in self.running_shaders:
            shader_id['rectangle'].pos = self.pos

    def _refresh_glsl(self, shader_id: ShaderIdType, _dt: float):
        """ timer/clock event handler to animate and sync one canvas shader. """
        self.refresh_shader(shader_id)

    def refresh_running_shaders(self):
        """ manually update all running_shaders. """
        for shader_id in self.running_shaders:
            self.refresh_shader(shader_id)

    def refresh_shader(self, shader_id: ShaderIdType) -> str:
        """ update the shader arguments for the current animation frame.

        :param shader_id:       dict with render context, rectangle and glsl input arguments.
        :return:                empty string if arguments got passed to the shader without errors, else error message.
        """
        ren_ctx = shader_id['render_ctx']
        start_time = shader_id['start_time']
        if callable(start_time):
            start_time = start_time()

        # first set the defaults for glsl fragment shader input args (uniforms)
        glsl_kwargs = shader_id['glsl_dyn_args']
        ren_ctx['alpha'] = 0.693
        ren_ctx['contrast'] = 0.696
        ren_ctx['win_pos'] = list(map(float, self.pos))
        ren_ctx['resolution'] = list(map(float, self.size))
        ren_ctx['tex_col_mix'] = 0.699
        if not callable(glsl_kwargs.get('time')):
            ren_ctx['time'] = Clock.get_boottime() - start_time

        # .. then overwrite glsl arguments with dynamic user values
        ret = ""
        for key, val in glsl_kwargs.items():
            try:
                ren_ctx[key] = val() if callable(val) else val
            except Exception as ex:
                ret += f"kivy_glsl.refresh_shader exception '{ex}' in arg {key}={val} - ignored!"
        return ret

    def _size_changed(self, *_args):
        """ size changed event handler. """
        for shader_id in self.running_shaders:
            shader_id['rectangle'].size = self.size

    def stop_shader(self, shader_id: ShaderIdType, set_run_state: bool = True):
        """ stop shader by removing it from started shaders.

        :param shader_id:       id of the shader to stop. ignoring if the passed shader got already stopped.
        :param set_run_state:   pass False to prevent that the `run_state` of the :paramref:`~stop_shader.shader_id`
                                gets changed to `paused` (for internal use to refresh all running shaders).
        """
        shaders = self.running_shaders
        if shader_id not in shaders:
            return              # ignore if app disabled rendering

        added_to = shader_id.pop('added_to')
        shader_id.pop('rectangle')
        ren_ctx = shader_id.pop('render_ctx')
        if added_to:
            added_to.remove(ren_ctx)
        else:
            self.canvas = None

        if 'timer' in shader_id:
            Clock.unschedule(shader_id.pop('timer'))

        if set_run_state:
            shader_id['run_state'] = 'paused'

        shaders.remove(shader_id)

    def update_shaders(self):
        """ stop/unbind all shaders, then restart/bind the shaders having their `run_state` as `'running'`. """
        for shader_id in reversed(self.running_shaders):
            self.stop_shader(shader_id, set_run_state=False)

        bound = self._pos_fbind_uid
        if self.added_shaders and self.parent:
            for shader_id in self.added_shaders:
                err_msg = ""
                if shader_id['run_state'] == 'running':
                    err_msg = self.play_shader(shader_id)
                    if not err_msg:
                        err_msg = self.refresh_shader(shader_id)
                shader_id['error_message'] = err_msg
                if err_msg:
                    shader_id['run_state'] = 'error'
            if not bound:
                self._pos_fbind_uid = self.fbind('pos', self._pos_changed)  # STRANGE: on_ event not bind-able -> ret==0
                self._size_fbind_uid = self.fbind('size', self._size_changed)
                self._pos_changed()
                self._size_changed()

        elif bound:
            self.unbind_uid('pos', self._pos_fbind_uid)
            self.unbind_uid('size', self._size_fbind_uid)
            self._pos_fbind_uid = 0
            self._size_fbind_uid = 0


Factory.register('ShadersMixin', cls=ShadersMixin)
