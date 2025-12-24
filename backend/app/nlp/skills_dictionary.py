from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class SkillEntry:
    name: str
    category: str
    aliases: tuple[str, ...]


SKILLS: dict[str, SkillEntry] = {
    # -----------------
    # Languages
    # -----------------
    "python": SkillEntry(
        name="Python",
        category="language",
        aliases=("python",),
    ),
    "javascript": SkillEntry(
        name="JavaScript",
        category="language",
        aliases=("javascript", "js"),
    ),
    "typescript": SkillEntry(
        name="TypeScript",
        category="language",
        aliases=("typescript", "ts"),
    ),
    "java": SkillEntry(
        name="Java",
        category="language",
        aliases=("java",),
    ),
    "csharp": SkillEntry(
        name="C#",
        category="language",
        aliases=("c#", "c sharp"),
    ),

    # -----------------
    # Frontend
    # -----------------
    "react": SkillEntry(
        name="React",
        category="frontend",
        aliases=("react", "react.js", "reactjs", "react js"),
    ),
    "nextjs": SkillEntry(
        name="Next.js",
        category="frontend",
        aliases=("nextjs", "next.js", "next js", "next"),
    ),
    "vue": SkillEntry(
        name="Vue",
        category="frontend",
        aliases=("vue", "vue.js", "vuejs", "vue js"),
    ),
    "nuxtjs": SkillEntry(
        name="Nuxt.js",
        category="frontend",
        aliases=("nuxt", "nuxtjs", "nuxt.js", "nuxt js"),
    ),
    "angular": SkillEntry(
        name="Angular",
        category="frontend",
        aliases=("angular",),
    ),

    # -----------------
    # Mobile Frontend
    # -----------------
    "reactnative": SkillEntry(
        name="React Native",
        category="mobile",
        aliases=("react native", "react-native", "reactnative"),
    ),

    # -----------------
    # Web Basics
    # -----------------
    "html": SkillEntry(
        name="HTML",
        category="web",
        aliases=("html", "html5"),
    ),
    "css": SkillEntry(
        name="CSS",
        category="web",
        aliases=("css", "css3"),
    ),
    "sass": SkillEntry(
        name="Sass",
        category="web",
        aliases=("sass", "scss"),
    ),

    # -----------------
    # Styling / UI Frameworks
    # -----------------
    "tailwindcss": SkillEntry(
        name="Tailwind CSS",
        category="styling",
        aliases=("tailwind", "tailwind css", "tailwindcss"),
    ),
    "materialui": SkillEntry(
        name="Material UI",
        category="styling",
        aliases=("material ui", "mui"),
    ),
    "shadcnui": SkillEntry(
        name="shadcn/ui",
        category="styling",
        aliases=("shadcn", "shadcn/ui", "shadcn ui"),
    ),
    "reactnativepaper": SkillEntry(
        name="React Native Paper",
        category="styling",
        aliases=("react native paper", "react-native-paper", "reactnativepaper"),
    ),
    "chakraui": SkillEntry(
        name="Chakra UI",
        category="styling",
        aliases=("chakra", "chakra ui", "chakra-ui"),
    ),
    "bootstrap": SkillEntry(
        name="Bootstrap",
        category="styling",
        aliases=("bootstrap",),
    ),

    # -----------------
    # Backend
    # -----------------
    "nodejs": SkillEntry(
        name="Node.js",
        category="backend",
        aliases=("node", "node.js", "nodejs"),
    ),
    "django": SkillEntry(
        name="Django",
        category="backend",
        aliases=("django",),
    ),
    "fastapi": SkillEntry(
        name="FastAPI",
        category="backend",
        aliases=("fastapi",),
    ),
    "spring": SkillEntry(
        name="Spring",
        category="backend",
        aliases=("spring", "spring boot"),
    ),

    # -----------------
    # Databases
    # -----------------
    "postgresql": SkillEntry(
        name="PostgreSQL",
        category="database",
        aliases=("postgres", "postgresql"),
    ),
    "mysql": SkillEntry(
        name="MySQL",
        category="database",
        aliases=("mysql",),
    ),
    "mongodb": SkillEntry(
        name="MongoDB",
        category="database",
        aliases=("mongodb", "mongo"),
    ),

    # -----------------
    # Cloud / DevOps
    # -----------------
    "aws": SkillEntry(
        name="AWS",
        category="cloud",
        aliases=("aws", "amazon web services"),
    ),
    "docker": SkillEntry(
        name="Docker",
        category="cloud",
        aliases=("docker",),
    ),
    "kubernetes": SkillEntry(
        name="Kubernetes",
        category="cloud",
        aliases=("kubernetes", "k8s"),
    ),

    # -----------------
    # Data / ML
    # -----------------
    "pandas": SkillEntry(
        name="Pandas",
        category="data",
        aliases=("pandas",),
    ),
    "numpy": SkillEntry(
        name="NumPy",
        category="data",
        aliases=("numpy",),
    ),
}
