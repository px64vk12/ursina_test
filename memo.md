ursina 
    panda3d를 쉽게 사용할 수 있도록 정리한 프레임워크
    https://www.ursinaengine.org/api_reference.html#textures



model clear
    position
    ratation
    scale


clear
controllor, update


clear
texture
    nodePath.setTexPos(TextureStage, uOffset, vOffset, wOffset)

clear
lighting
    디렉셔널 : 모든 빛이 같다. 멀리서 같은 방향으로 오는 빛 구현
    스카이 : 천장을 광원으로 만든다.
    스포트 : 원뿔모양으로 빛을 만든다.
    포인트 : 모든방향으로 빛을 만든다.


particle effect
    타격, 불 및 파편 등 이펙트, lighting


맵 그리드 : 오픈월드, 200m 이내만 로딩 그리기
맵 에디터


엑터 : 
    1. 캐릭터 조인트 본
    2. 레그돌 적용
    3. 바스트 모핑 : https://discourse.panda3d.org/t/hair-physics-simulation/28055


렌더링 파이프라인 : 머티리얼, 리플렉션 구현
https://github.com/tobspr/RenderPipeline
https://github.com/tobspr/RenderPipeline/wiki/Getting%20Started