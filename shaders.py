#En OpenGl, los shaders se escriben
#en un nuevo lenguaje llamado GLSL
#(Graphics Library Shaders Language)

vertex_shader= '''
#version 450 core

layout(location=0) in vec3 position;
layout(location=1) in vec2 texCoords;
layout(location=2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 outNormals;

void main()
{   
    outNormals = (modelMatrix * vec4(normals,0.0)).xyz;
    outNormals = normalize(outNormals);

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    UVs = texCoords;
}
'''

vibing_shader= '''
#version 450 core

layout(location=0) in vec3 position;
layout(location=1) in vec2 texCoords;
layout(location=2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 outNormals;

void main()
{
    vec3 pos = position;
    pos.y += sin(time + pos.x + pos.z)/2;
    
    outNormals = (modelMatrix * vec4(normals,0.0)).xyz;
    outNormals = normalize(outNormals);
    
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1.0);
    UVs = texCoords;
}
'''

fat_shader= '''
#version 450 core

layout(location=0) in vec3 position;
layout(location=1) in vec2 texCoords;
layout(location=2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float fatness;

out vec2 UVs;
out vec3 outNormals;

void main()
{   
    outNormals = (modelMatrix * vec4(normals,0.0)).xyz;
    outNormals = normalize(outNormals);
    vec3 pos = position + (fatness/4) * outNormals;
    
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1.0);
    UVs = texCoords;
}
'''

fragment_shader = '''
#version 450 core

layout(binding = 0) uniform sampler2D tex;

in vec2 UVs;
in vec3 outNormals;

out vec4 fragColor;

void main()
{
    fragColor = texture(tex, UVs);
}
'''

gourad_shader = '''
#version 450 core

layout(binding = 0) uniform sampler2D tex;

uniform vec3 dirLight;

in vec2 UVs;
in vec3 outNormals;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, -dirLight);
    fragColor = texture(tex, UVs) * intensity;
}
'''

toon_shader = '''
#version 450 core

layout(binding = 0) uniform sampler2D tex;

uniform vec3 dirLight;

in vec2 UVs;
in vec3 outNormals;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, -dirLight);
    
    if (intensity < 0.3)
        intensity = 0.2;
    else if (intensity < 0.66)
        intensity = 0.6;
    else
        intensity = 1.0;
        
    fragColor = texture(tex, UVs) * intensity;
}
'''

#vec4 newPos = vec4(position.x, position.y + sin(time + position.x)/2, position.z, 1.0);
""" layout(binding = 0) uniform sampler2D tex;

uniform vec3 dirLight;

in vec2 UVs;
in vec3 outNormals;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, -dirLight);
    intensity = min(1,intensity);
    intensity = max(0,intensity);
    fragColor = texture(tex, UVs) * intensity;
} """