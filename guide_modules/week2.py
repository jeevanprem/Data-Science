# -*- coding: utf-8 -*-
"""Week 2 Module: Linear Algebra for Data Science"""

def get_week2_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 2 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week2">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 02</span> Linear Algebra for Data Science</h2>
                    <div class="module-lectures">NPTEL Lectures 12–18 | Linear Systems, Rank, Vector Spaces, Span, Norms, Hyperplanes, Eigenvalues &amp; Eigenvectors</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        Linear algebra forms the foundational mathematical engine of data science. Datasets are organized as matrices $X \\in \\mathbb{R}^{n \\times p}$ (samples by features), geometric distances govern clustering and nearest neighbors, transformations rely on matrix-vector products, and spectral decomposition (eigenvalues/eigenvectors) underpins Principal Component Analysis (PCA) and dimensionality reduction.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Systems of Linear Equations, Rank &amp; Consistency Conditions</h4>
                        <p>
                            Consider the matrix-vector system $Ax = b$, where $A \\in \\mathbb{R}^{m \\times n}$ is the coefficient matrix, $x \\in \\mathbb{R}^{n \\times 1}$ is the unknown variable vector, and $b \\in \\mathbb{R}^{m \\times 1}$ is the target vector. We construct the augmented matrix $[A \\mid b] \\in \\mathbb{R}^{m \\times (n+1)}$.
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Rouché–Capelli Theorem:</strong>
                                <ul style="margin-left: 18px; margin-top: 4px;">
                                    <li><strong>Inconsistent System (No Solution):</strong> $\\text{rank}(A) &lt; \\text{rank}([A \\mid b])$. The target vector $b$ lies outside the column space of $A$.</li>
                                    <li><strong>Consistent System:</strong> $\\text{rank}(A) = \\text{rank}([A \\mid b])$.
                                        <br>• <strong>Unique Solution:</strong> $\\text{rank}(A) = \\text{rank}([A \\mid b]) = n$ (number of variables). The columns of $A$ are linearly independent.
                                        <br>• <strong>Infinitely Many Solutions:</strong> $\\text{rank}(A) = \\text{rank}([A \\mid b]) &lt; n$. There exist $n - \\text{rank}(A)$ free variables / degrees of freedom.
                                    </li>
                                </ul>
                            </li>
                            <li><strong>Rank Properties:</strong> The maximum number of linearly independent rows or columns. For an $m \\times n$ matrix: $\\text{rank}(A) \\le \\min(m, n)$. Furthermore, $\\text{rank}(A B) \\le \\min(\\text{rank}(A), \\text{rank}(B))$ and $\\text{rank}(A^T A) = \\text{rank}(A A^T) = \\text{rank}(A)$.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. Overdetermined vs Underdetermined Systems &amp; Pseudoinverses</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Overdetermined Systems ($m &gt; n$):</strong> More equations (measurements) than unknown parameters. Usually inconsistent due to real-world noise.
                                <br>• <em>Ordinary Least Squares (OLS) Solution:</em> Minimizes squared residual error $\\|Ax - b\\|_2^2$. The normal equations are $(A^T A)x = A^T b$.
                                <br>• If $A$ has full column rank $n$, $(A^T A)$ is invertible. The unique least-squares solution is:
                                $$\hat{x} = (A^T A)^{-1} A^T b = A^+_{\\text{left}} b$$
                                where $A^+_{\\text{left}} = (A^T A)^{-1} A^T$ is the <strong>left Moore–Penrose pseudoinverse</strong> ($A^+ A = I_n$).
                            </li>
                            <li><strong>Underdetermined Systems ($m &lt; n$):</strong> More variables than equations (e.g. genomic data where $p \\gg n$). If $\\text{rank}(A) = m$, infinitely many exact solutions exist.
                                <br>• <em>Minimum-Norm Solution:</em> Finds the solution $x$ satisfying $Ax = b$ with the smallest Euclidean length $\\|x\\|_2$.
                                <br>• Formula using <strong>right pseudoinverse</strong>:
                                $$\hat{x} = A^T (A A^T)^{-1} b = A^+_{\\text{right}} b$$
                                where $A A^+_{\\text{right}} = I_m$.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. Vector Spaces, Linear Span, and Basis</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Linear Combination:</strong> A vector $v = c_1 v_1 + c_2 v_2 + \\dots + c_k v_k$ for scalars $c_i \\in \\mathbb{R}$.</li>
                            <li><strong>Linear Span:</strong> $\\text{span}\\{v_1, \\dots, v_k\\}$ is the set of all possible linear combinations.
                                <br><em>Spanning Criterion for $\\mathbb{R}^n$:</em> A set of $k$ vectors in $\\mathbb{R}^n$ spans $\\mathbb{R}^n$ if and only if the matrix formed by taking these vectors as columns has rank equal to $n$. Note: It requires at least $k \\ge n$ vectors to span $\\mathbb{R}^n$. If $k = n$, this requires $\\det([v_1, \\dots, v_n]) \\ne 0$.</li>
                            <li><strong>Linear Independence:</strong> Vectors $\\{v_1, \\dots, v_k\\}$ are linearly independent if $c_1 v_1 + \\dots + c_k v_k = 0 \\implies c_1 = c_2 = \\dots = c_k = 0$. In $\\mathbb{R}^n$, any collection of more than $n$ vectors ($k &gt; n$) is guaranteed to be linearly dependent!</li>
                            <li><strong>Basis &amp; Dimension:</strong> A basis of a vector space is a linearly independent spanning set. The dimension of $\\mathbb{R}^n$ is exactly $n$. Any basis of $\\mathbb{R}^n$ must contain precisely $n$ linearly independent vectors.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Vector Norms, Angles, Hyperplanes &amp; Halfspaces</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>$L_1$ Norm (Manhattan):</strong> $\\|x\\|_1 = \\sum_{i=1}^n |x_i|$. Sum of absolute coordinate distances (used in Lasso regression).</li>
                            <li><strong>$L_2$ Norm (Euclidean):</strong> $\\|x\\|_2 = \\sqrt{\\sum_{i=1}^n x_i^2} = \\sqrt{x^T x}$. Standard geometric distance (used in Ridge regression and KNN).</li>
                            <li><strong>$L_\\infty$ Norm (Chebyshev / Max):</strong> $\\|x\\|_\\infty = \\max_{1 \\le i \\le n} |x_i|$.</li>
                            <li><strong>Inner Product &amp; Orthogonality:</strong> $\\langle u, v \\rangle = u^T v = \\|u\\|_2 \\|v\\|_2 \\cos \\theta$. Two non-zero vectors are orthogonal ($u \\perp v$) if and only if $u^T v = 0$ (i.e. $\\cos \\theta = 0$).</li>
                            <li><strong>Hyperplanes &amp; Halfspaces:</strong> A hyperplane in $\\mathbb{R}^n$ is defined as $\\mathcal{H} = \\{x \\in \\mathbb{R}^n \\mid w^T x + b = 0\\}$, where $w$ is the normal vector orthogonal to the plane.
                                <br>• <em>Perpendicular Distance from Point $x_0$ to Hyperplane:</em>
                                $$d(x_0, \\mathcal{H}) = \\frac{|w^T x_0 + b|}{\\|w\\|_2}$$
                                • The hyperplane partitions $\\mathbb{R}^n$ into two opposing halfspaces: $w^T x + b &gt; 0$ and $w^T x + b &lt; 0$. This is the geometric engine of linear classification and Support Vector Machines (SVM).
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. Spectral Theory: Eigenvalues and Eigenvectors</h4>
                        <p>
                            For a square matrix $A \\in \\mathbb{R}^{n \\times n}$, a non-zero vector $v \\ne 0$ is an <strong>eigenvector</strong> associated with <strong>eigenvalue</strong> $\\lambda$ if:
                            $$A v = \\lambda v \\iff (A - \\lambda I) v = 0$$
                            For a non-trivial solution ($v \\ne 0$) to exist, the matrix $(A - \\lambda I)$ must be singular:
                            $$\\det(A - \\lambda I) = 0 \\quad \\text{(Characteristic Polynomial)}$$
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Trace Theorem:</strong> $\\sum_{i=1}^n \\lambda_i = \\text{trace}(A) = \\sum_{i=1}^n A_{ii}$. (Sum of eigenvalues equals sum of diagonal elements).</li>
                            <li><strong>Determinant Theorem:</strong> $\\prod_{i=1}^n \\lambda_i = \\det(A)$. (Product of eigenvalues equals determinant).</li>
                            <li><strong>Matrix Polynomial Shift Theorem:</strong> If $A$ has eigenvalues $\\lambda_1, \\dots, \\lambda_n$, then $(A - cI)$ has eigenvalues $(\\lambda_1 - c), \\dots, (\\lambda_n - c)$.
                                <br>Consequently: $\\det(A - cI) = \\prod_{i=1}^n (\\lambda_i - c)$.
                            </li>
                            <li><strong>Matrix Inversion:</strong> If $A$ is invertible (no zero eigenvalue), $A^{-1}$ has eigenvalues $1/\\lambda_i$. Furthermore, $\\det(A^{-1}) = \\frac{1}{\\det(A)}$ and $\\det((A^{-1})^T) = \\det(A^{-1})$.</li>
                            <li><strong>Scalar Multiplication:</strong> For scalar $c$ and $n \\times n$ matrix $A$, eigenvalues of $c A$ are $c \\lambda_i$, and $\\det(c A) = c^n \\det(A)$.</li>
                            <li><strong>Symmetric Matrices ($A = A^T$):</strong> All eigenvalues are strictly real, and eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">F. Rank-1 Outer Product Matrices &amp; NPTEL Special Identities</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Outer Product $M = u u^T$:</strong> For non-zero column vector $u = [u_1, \\dots, u_n]^T \\in \\mathbb{R}^n$, the outer product matrix $M = u u^T$ has $\\text{rank}(M) = 1$.
                                <br>• Notice: $M u = (u u^T) u = u (u^T u) = (\\|u\\|_2^2) u$. Thus $u$ is an eigenvector with eigenvalue $\\lambda_1 = \\|u\\|_2^2 = \\sum_{i=1}^n u_i^2 = \\text{trace}(M)$.
                                <br>• Since $\\text{rank}(M) = 1$, all remaining $n-1$ eigenvalues are exactly zero: $\\lambda_2 = \\dots = \\lambda_n = 0$.
                            </li>
                            <li><strong>Assignment Pattern ($A = [a, b, c]^T$):</strong> For matrix $M = A A^T = \\begin{bmatrix} a^2 &amp; ab &amp; ac \\\\ ab &amp; b^2 &amp; bc \\\\ ac &amp; bc &amp; c^2 \\end{bmatrix}$, its eigenvalues are $\\lambda_1 = a^2 + b^2 + c^2$, $\\lambda_2 = 0$, $\\lambda_3 = 0$.
                                <br>• Sum of pairwise products: $\\lambda_1\\lambda_2 + \\lambda_2\\lambda_3 + \\lambda_3\\lambda_1 = 0 + 0 + 0 = 0$.
                            </li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Inverting Zero Eigenvalues &amp; Matrix Dimensions</h4>
                            <p>
                                <strong>Trap 1:</strong> The statement <em>"If $\\lambda$ is an eigenvalue of $A$, then $1/\\lambda$ is always an eigenvalue of $A^{-1}$"</em> is only true if $\\det(A) \\ne 0$. If $A$ is singular ($\lambda = 0$), $A^{-1}$ does not exist!
                                <br><strong>Trap 2:</strong> To find $\\det(A - 2I)$ when given the eigenvalues of $A$, students often attempt to reconstruct matrix $A$. <strong>Never do this!</strong> Simply subtract 2 from each eigenvalue and multiply: $\\det(A - 2I) = (\\lambda_1 - 2)(\\lambda_2 - 2)\\dots(\\lambda_n - 2)$.
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's 10-Second Shortcut: Eigenvalues of a 2x2 Matrix</h4>
                            <p>
                                For any $2 \\times 2$ matrix $M$, the characteristic polynomial is universally:
                                $$\\lambda^2 - \\text{trace}(M)\\lambda + \\det(M) = 0$$
                                If the problem gives you $\\text{trace}(M) = 4$ and $\\det(M) = 3$, solve instantly:
                                $$\\lambda^2 - 4\\lambda + 3 = 0 \\implies (\\lambda - 1)(\\lambda - 3) = 0 \\implies \\lambda_1 = 1, \\; \\lambda_2 = 3.$$
                                No matrix expansion required!
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Mathematical Formulas &amp; Spectral Identities</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Linear System Consistency</span>
                                <span class="nav-badge">Rouché-Capelli</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{rank}(A) = \\text{rank}([A \\mid b])$$
                            </div>
                            <div class="formula-desc">System $Ax = b$ is consistent iff augmented matrix rank equals coefficient matrix rank. Unique if rank $= n$; infinite if rank $&lt; n$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> A system of 3 variables has $\\text{rank}(A) = 2$ and $\\text{rank}([A \\mid b]) = 3$. How many solutions exist?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Since $\\text{rank}(A) \\ne \\text{rank}([A \\mid b])$, the system is inconsistent. There are $0$ solutions (no solution).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If $\\text{rank}(A) = \\text{rank}([A \\mid b]) = 2$ for $n = 3$ variables, what is the nature of solutions?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Ranks match, so system is consistent. Because $\\text{rank} &lt; n$, there are infinitely many solutions parameterized by $n - \\text{rank} = 3 - 2 = 1$ free variable.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Eigenvalue Trace &amp; Det Identities</span>
                                <span class="nav-badge">Spectral</span>
                            </div>
                            <div class="formula-math">
                                $$\\sum_{i=1}^n \\lambda_i = \\text{tr}(A), \\quad \\prod_{i=1}^n \\lambda_i = \\det(A)$$
                            </div>
                            <div class="formula-desc">Sum of eigenvalues equals the matrix trace (sum of diagonal entries). Product of eigenvalues equals the matrix determinant.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> A $3 \\times 3$ matrix $A$ has $\\text{tr}(A) = 9$, $\\det(A) = 24$, and known eigenvalues $\\lambda_1 = 2, \\lambda_2 = 3$. Find $\\lambda_3$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Trace property: $2 + 3 + \\lambda_3 = 9 \\implies \\lambda_3 = 4$. Verification via determinant: $2 \\times 3 \\times 4 = 24$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> A $2 \\times 2$ matrix has trace $5$ and determinant $6$. What are its eigenvalues?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Characteristic equation is $\\lambda^2 - 5\\lambda + 6 = 0 \\implies (\\lambda - 2)(\\lambda - 3) = 0 \\implies \\lambda_1 = 2, \\; \\lambda_2 = 3$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Determinant of Shifted Matrix</span>
                                <span class="nav-badge">Spectral Theorem</span>
                            </div>
                            <div class="formula-math">
                                $$\\det(A - cI) = \\prod_{i=1}^n (\\lambda_i - c)$$
                            </div>
                            <div class="formula-desc">The determinant of $(A - cI)$ is simply the product of each eigenvalue shifted by constant $c$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Matrix $A$ has eigenvalues $4$ and $7$. What is $\\det(A - 3I)$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Shift each eigenvalue by $3$: $(\\lambda_1 - 3)(\\lambda_2 - 3) = (4 - 3)(7 - 3) = 1 \\times 4 = 4$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If matrix $M$ has eigenvalues $-1, 2, 5$, what is $\\det(M + 2I)$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $M + 2I = M - (-2)I$, so shift eigenvalues by $+2$: $(-1 + 2)(2 + 2)(5 + 2) = 1 \\times 4 \\times 7 = 28$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Orthogonality Condition</span>
                                <span class="nav-badge">Geometry</span>
                            </div>
                            <div class="formula-math">
                                $$u^T v = \\sum_{i=1}^n u_i v_i = 0$$
                            </div>
                            <div class="formula-desc">Two non-zero vectors $u$ and $v$ are orthogonal if and only if their Euclidean inner product vanishes.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> For what value of $k$ are $u = [1, k, 3]^T$ and $v = [4, -2, 2]^T$ orthogonal?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Set $u^T v = 0 \\implies (1)(4) + (k)(-2) + (3)(2) = 0 \\implies 4 - 2k + 6 = 0 \\implies 2k = 10 \\implies k = 5$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Are columns $q_1 = [3/5, 4/5]^T$ and $q_2 = [-4/5, 3/5]^T$ orthonormal?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Dot product $(3/5)(-4/5) + (4/5)(3/5) = 0$ (orthogonal). Lengths $\|q_1\| = \\sqrt{9/25+16/25} = 1$, $\|q_2\| = 1$. Yes, orthonormal.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Point-to-Hyperplane Distance</span>
                                <span class="nav-badge">Geometry</span>
                            </div>
                            <div class="formula-math">
                                $$d(x_0, \\mathcal{H}) = \\frac{|w^T x_0 + b|}{\\|w\\|_2}$$
                            </div>
                            <div class="formula-desc">Perpendicular Euclidean distance from point $x_0$ to hyperplane $w^T x + b = 0$. Sign of $w^T x_0 + b$ indicates the halfspace.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Find distance from $x_0 = [1, 2]^T$ to line $3x_1 + 4x_2 - 6 = 0$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Normal vector $w = [3, 4]^T$, so $\\|w\\|_2 = \\sqrt{3^2 + 4^2} = 5$. Numerator: $|3(1) + 4(2) - 6| = |5| = 5$. Thus $d = 5/5 = 1$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Do points $[0, 0]^T$ and $[2, 1]^T$ lie in the same halfspace of $2x_1 - x_2 + 4 = 0$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> At origin: $2(0) - (0) + 4 = +4 &gt; 0$. At $[2, 1]^T$: $2(2) - 1 + 4 = +7 &gt; 0$. Both yield positive signs, so yes, they lie in the same halfspace.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Moore-Penrose Pseudoinverses</span>
                                <span class="nav-badge">Least Squares</span>
                            </div>
                            <div class="formula-math">
                                $$A^+_{\\text{left}} = (A^T A)^{-1} A^T, \\quad A^+_{\\text{right}} = A^T (A A^T)^{-1}$$
                            </div>
                            <div class="formula-desc">Left pseudoinverse solves overdetermined OLS $\\min \\|Ax-b\\|^2$; right pseudoinverse finds minimum-norm solution for underdetermined systems.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Given overdetermined system $x = 2$ and $2x = 3$, find the least squares estimate $\hat{x}$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Matrix $A = [1, 2]^T$, $b = [2, 3]^T$. $A^T A = 1^2 + 2^2 = 5$, and $A^T b = 1(2) + 2(3) = 8$. Thus $\hat{x} = (A^T A)^{-1} A^T b = 8/5 = 1.6$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> When does $(A^T A)^{-1}$ exist for an $m \\times n$ matrix with $m &gt; n$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $(A^T A)$ of size $n \\times n$ is non-singular and invertible if and only if $A$ has full column rank $n$ (linearly independent columns).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Rank-1 Outer Product Eigenvalues</span>
                                <span class="nav-badge">Spectral Theorem</span>
                            </div>
                            <div class="formula-math">
                                $$M = u u^T \\implies \\lambda_1 = \\|u\\|_2^2, \\quad \\lambda_2 = \\dots = \\lambda_n = 0$$
                            </div>
                            <div class="formula-desc">The outer product of vector $u \\in \\mathbb{R}^n$ with itself has rank 1. Its only non-zero eigenvalue is $\\|u\\|^2 = \\text{tr}(M)$. All other $n-1$ eigenvalues equal 0.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Find all eigenvalues of $M = u u^T$ for $u = [1, 2, 2]^T$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\lambda_1 = 1^2 + 2^2 + 2^2 = 9$. Because $\\text{rank}(M) = 1$, the other two eigenvalues are $\\lambda_2 = 0, \\lambda_3 = 0$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For $M = A A^T$ where $A = [a, b, c]^T$, what is the sum of pairwise products $\\sum_{i &lt; j} \\lambda_i \\lambda_j$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Eigenvalues are $(a^2+b^2+c^2, 0, 0)$. Each pair includes at least one zero eigenvalue, so $\\lambda_1\\lambda_2 + \\lambda_2\\lambda_3 + \\lambda_3\\lambda_1 = 0$.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Linear Algebra Functions</h3>
                    <div class="table-responsive">
                        <table class="academic-table">
                            <thead>
                                <tr>
                                    <th>Function / Syntax</th>
                                    <th>Signature &amp; Arguments</th>
                                    <th>Mathematical Operation</th>
                                    <th>Practical Code Example</th>
                                    <th>Output / Return Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="code-cell">%*%</span></td>
                                    <td><code class="inline-code">A %*% B</code></td>
                                    <td>Matrix product $A B$</td>
                                    <td><code class="inline-code">matrix(1:4,2) %*% c(1,2)</code></td>
                                    <td>Column vector $[7, 10]^T$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">t()</span></td>
                                    <td><code class="inline-code">t(x)</code></td>
                                    <td>Matrix transpose $A^T$</td>
                                    <td><code class="inline-code">t(matrix(1:4, 2, 2))</code></td>
                                    <td>Transposed $2 \\times 2$ matrix</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">solve()</span></td>
                                    <td><code class="inline-code">solve(a, b)</code></td>
                                    <td>Solves $Ax = b$; if $b$ omitted, computes $A^{-1}$</td>
                                    <td><code class="inline-code">solve(matrix(c(1,1,1,2),2,2), c(3,5))</code></td>
                                    <td>Solution vector $[1, 2]^T$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">det()</span></td>
                                    <td><code class="inline-code">det(x)</code></td>
                                    <td>Computes matrix determinant $\det(A)$</td>
                                    <td><code class="inline-code">det(matrix(c(1,1,1,2), 2, 2))</code></td>
                                    <td><code class="inline-code">1</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">eigen()</span></td>
                                    <td><code class="inline-code">eigen(x, symmetric)</code></td>
                                    <td>Calculates eigenvalues and eigenvectors of square matrix</td>
                                    <td><code class="inline-code">ev &lt;- eigen(A); ev$values; ev$vectors</code></td>
                                    <td>List with <code class="inline-code">$values</code> and <code class="inline-code">$vectors</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">qr()$rank</span></td>
                                    <td><code class="inline-code">qr(x)$rank</code></td>
                                    <td>Determines the numerical rank of a matrix via QR decomposition</td>
                                    <td><code class="inline-code">qr(matrix(c(1,2,2,4), 2, 2))$rank</code></td>
                                    <td><code class="inline-code">1</code> (since col 2 = $2 \\times$ col 1)</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">diag()</span></td>
                                    <td><code class="inline-code">diag(x)</code></td>
                                    <td>Extracts diagonal or creates identity / diagonal matrix</td>
                                    <td><code class="inline-code">diag(3)</code></td>
                                    <td>$3 \\times 3$ identity matrix $I_3$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">norm()</span></td>
                                    <td><code class="inline-code">norm(x, type = c("O", "I", "F", "2"))</code></td>
                                    <td>Calculates matrix norm ($1$-norm, $\\infty$-norm, Frobenius)</td>
                                    <td><code class="inline-code">norm(matrix(1:4, 2), "F")</code></td>
                                    <td>Frobenius norm $\\sqrt{1+4+9+16} = 5.477$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">ginv()</span></td>
                                    <td><code class="inline-code">MASS::ginv(X, tol)</code></td>
                                    <td>Computes the Moore–Penrose generalized pseudoinverse $X^+$ via SVD.</td>
                                    <td><code class="inline-code">library(MASS); ginv(A)</code></td>
                                    <td>Pseudoinverse matrix $A^+$ of size $n \\times m$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">crossprod() / tcrossprod()</span></td>
                                    <td><code class="inline-code">crossprod(x, y), tcrossprod(x, y)</code></td>
                                    <td>Efficient computation of $x^T y$ and $x y^T$ without explicit transpose.</td>
                                    <td><code class="inline-code">crossprod(X); tcrossprod(u)</code></td>
                                    <td>$X^T X$ matrix / outer product $u u^T$</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 4: Topic-Wise Example Questions with Solutions -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 4. Topic-Wise Example Questions with Solutions</h3>

                    <!-- Question 1 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Vector Span in R^2</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Does the set $S = \\{(1, 1), (1, 2)\\}$ span $\\mathbb{R}^2$?</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> Yes</li>
                                <li><span class="opt-bullet">B.</span> No</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Method 1: First-Principles Linear Combination Test</div>
                                    <p>
                                        To span $\\mathbb{R}^2$, any arbitrary vector $(x, y) \\in \\mathbb{R}^2$ must be expressible as:
                                        $$a(1, 1) + b(1, 2) = (x, y)$$
                                        Equating components:
                                        $$a + b = x \\quad \\text{and} \\quad a + 2b = y$$
                                        Subtracting the first equation from the second:
                                        $$b = y - x$$
                                        Substituting back into $a + b = x$:
                                        $$a = x - b = x - (y - x) = 2x - y$$
                                        Since unique real scalars $a = 2x - y$ and $b = y - x$ exist for <em>every</em> $(x, y) \\in \\mathbb{R}^2$, the set $S$ spans $\\mathbb{R}^2$.
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Method 2: Determinant &amp; Rank Shortcut</div>
                                    <p>
                                        Form the matrix with vectors as columns:
                                        $$A = \\begin{bmatrix} 1 &amp; 1 \\ 1 &amp; 2 \\end{bmatrix}$$
                                        $$\\det(A) = (1)(2) - (1)(1) = 2 - 1 = 1 \\ne 0$$
                                        Since $\\det(A) \\ne 0$, the vectors are linearly independent. Because there are 2 linearly independent vectors in a 2-dimensional space $\\mathbb{R}^2$, they form a basis and span $\\mathbb{R}^2$.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (Yes)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Eigenvalues from Trace &amp; Determinant</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> Let $M$ be a $2 \\times 2$ real matrix with $\\text{trace}(M) = 4$ and $\\det(M) = 3$. Find the eigenvalues of $M$.</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $\\lambda = 2, 2$</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> $\\lambda = 1, 3$</li>
                                <li><span class="opt-bullet">C.</span> $\\lambda = 4, 3$</li>
                                <li><span class="opt-bullet">D.</span> $\\lambda = -1, -3$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Set Up Characteristic Equation</div>
                                    <p>For any $2 \\times 2$ matrix, the characteristic equation is:
                                    $$\\lambda^2 - \\text{tr}(M)\\lambda + \\det(M) = 0$$
                                    Substituting the given values:
                                    $$\\lambda^2 - 4\\lambda + 3 = 0$$
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Factorize and Solve</div>
                                    <p>
                                    $$(\\lambda - 1)(\\lambda - 3) = 0 \\implies \\lambda_1 = 1, \\quad \\lambda_2 = 3$$
                                    <em>Verification:</em>
                                    <br>Sum: $\\lambda_1 + \\lambda_2 = 1 + 3 = 4 = \\text{trace}(M)$ (matches).
                                    <br>Product: $\\lambda_1 \\times \\lambda_2 = 1 \\times 3 = 3 = \\det(M)$ (matches).
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B ($\lambda = 1, 3$)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Determinant of Shifted Polynomial Matrix</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> Suppose the eigenvalues of a $4 \\times 4$ matrix $A$ are $-3, -4, -4, -3$. Find the determinant of the matrix $(A - 2I)$.</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $144$</li>
                                <li><span class="opt-bullet">B.</span> $-900$</li>
                                <li class="correct-option"><span class="opt-bullet">C.</span> $900$</li>
                                <li><span class="opt-bullet">D.</span> $0$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Apply the Spectral Shift Property</div>
                                    <p>
                                        If $\\lambda$ is an eigenvalue of $A$ with eigenvector $v$, then:
                                        $$(A - 2I) v = A v - 2 v = \\lambda v - 2 v = (\\lambda - 2) v$$
                                        Therefore, the eigenvalues of $(A - 2I)$ are $(\\lambda_i - 2)$ for each eigenvalue of $A$.
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Calculate Shifted Eigenvalues</div>
                                    <p>
                                        Given $\\lambda(A) = \\{-3, -4, -4, -3\\}$:
                                        $$\\mu_1 = -3 - 2 = -5$$
                                        $$\\mu_2 = -4 - 2 = -6$$
                                        $$\\mu_3 = -4 - 2 = -6$$
                                        $$\\mu_4 = -3 - 2 = -5$$
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 3: Compute Determinant via Product of Eigenvalues</div>
                                    <p>
                                        $$\\det(A - 2I) = \\prod_{i=1}^4 \\mu_i = (-5) \\times (-6) \\times (-6) \\times (-5)$$
                                        $$\\det(A - 2I) = 30 \\times 30 = 900$$
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option C ($900$)
                                </div>
                            </div>
                        </details>
                    </div>
                </section>

                <!-- Section 5: Dedicated Assignment-Style Practice Question -->
                <section class="section-block">
                    <div class="assignment-showcase">
                        <div class="assignment-banner">
                            <span>📝 DEDICATED ASSIGNMENT-STYLE PRACTICE CHALLENGE</span>
                            <span>Week 2 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: System Consistency Analysis &amp; Rank Determination
                            </p>
                            <p>
                                Consider the following system of 3 linear equations in 3 variables $(x_1, x_2, x_3)$:
                                $$\\begin{aligned}
                                x_1 + 2x_2 + 3x_3 &amp;= 1 \\
                                2x_1 + 5x_2 + 7x_3 &amp;= 2 \\
                                2x_1 + 4x_2 + 6x_3 &amp;= 2
                                \\end{aligned}$$
                            </p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>Formulate the augmented matrix $[A \\mid b]$ and reduce it to Row Echelon Form (REF) using elementary row operations.</li>
                                <li>Determine the rank of the coefficient matrix $A$ and the rank of the augmented matrix $[A \\mid b]$.</li>
                                <li>Conclude whether the system has a unique solution, infinitely many solutions, or no solution. If infinitely many solutions exist, express the general solution in parametric vector form.</li>
                                <li>Write the complete R code to verify the ranks using <code class="inline-code">qr()$rank</code>.</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Set Up Augmented Matrix and Apply Row Operations</div>
                                        <p>
                                            $$[A \\mid b] = \\begin{bmatrix}
                                            1 &amp; 2 &amp; 3 &amp; \\big| &amp; 1 \\
                                            2 &amp; 5 &amp; 7 &amp; \\big| &amp; 2 \\
                                            2 &amp; 4 &amp; 6 &amp; \\big| &amp; 2
                                            \\end{bmatrix}$$
                                            Apply row operations:
                                            <br>• $R_2 \\leftarrow R_2 - 2R_1$:
                                            $$\\begin{bmatrix} 2 &amp; 5 &amp; 7 &amp; 2 \\end{bmatrix} - \\begin{bmatrix} 2 &amp; 4 &amp; 6 &amp; 2 \\end{bmatrix} = \\begin{bmatrix} 0 &amp; 1 &amp; 1 &amp; 0 \\end{bmatrix}$$
                                            • $R_3 \\leftarrow R_3 - 2R_1$:
                                            $$\\begin{bmatrix} 2 &amp; 4 &amp; 6 &amp; 2 \\end{bmatrix} - \\begin{bmatrix} 2 &amp; 4 &amp; 6 &amp; 2 \\end{bmatrix} = \\begin{bmatrix} 0 &amp; 0 &amp; 0 &amp; 0 \\end{bmatrix}$$
                                            Resulting Row Echelon Form:
                                            $$[A_{\\text{ref}} \\mid b_{\\text{ref}}] = \\begin{bmatrix}
                                            1 &amp; 2 &amp; 3 &amp; \\big| &amp; 1 \\
                                            0 &amp; 1 &amp; 1 &amp; \\big| &amp; 0 \\
                                            0 &amp; 0 &amp; 0 &amp; \\big| &amp; 0
                                            \\end{bmatrix}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: Rank Determination</div>
                                        <p>
                                            Counting the non-zero rows in REF:
                                            <br>• In matrix $A_{\\text{ref}}$: Rows 1 and 2 are non-zero; row 3 is all zeros $\\implies \\mathbf{\\text{rank}(A) = 2}$.
                                            <br>• In augmented matrix $[A_{\\text{ref}} \\mid b_{\\text{ref}}]$: Rows 1 and 2 are non-zero; row 3 is all zeros $\\implies \\mathbf{\\text{rank}([A \\mid b]) = 2}$.
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Consistency &amp; Parametric Solution</div>
                                        <p>
                                            Since $\\text{rank}(A) = \\text{rank}([A \\mid b]) = 2 &lt; n = 3$ (number of variables), by the Rouché–Capelli theorem, the system is <strong>consistent with infinitely many solutions</strong>.
                                            <br>Degrees of freedom $= n - \\text{rank}(A) = 3 - 2 = 1$ free variable.
                                            <br>Let $x_3 = t \\in \\mathbb{R}$ (free parameter).
                                            <br>From Row 2: $x_2 + x_3 = 0 \\implies x_2 = -t$.
                                            <br>From Row 1: $x_1 + 2x_2 + 3x_3 = 1 \\implies x_1 + 2(-t) + 3t = 1 \\implies x_1 + t = 1 \\implies x_1 = 1 - t$.
                                            <br>In vector form:
                                            $$\\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\end{bmatrix} = \\begin{bmatrix} 1 \\ 0 \\ 0 \\end{bmatrix} + t \\begin{bmatrix} -1 \\ -1 \\ 1 \\end{bmatrix}, \\quad t \\in \\mathbb{R}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: R Code Implementation &amp; Verification</div>
                                        <pre class="r-code"># Coefficient Matrix and RHS Vector
A &lt;- matrix(c(1, 2, 2, 
              2, 5, 4, 
              3, 7, 6), nrow = 3, ncol = 3)
b &lt;- c(1, 2, 2)
Aug &lt;- cbind(A, b)

# Verify Ranks
rank_A &lt;- qr(A)$rank
rank_Aug &lt;- qr(Aug)$rank

cat("Rank(A):", rank_A, "\\n")      # Output: 2
cat("Rank([A|b]):", rank_Aug, "\\n") # Output: 2
cat("Consistent?", rank_A == rank_Aug, "\\n")
cat("Infinite solutions?", rank_A &lt; ncol(A), "\\n")</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Conclusion: rank(A) = 2, rank([A|b]) = 2. Consistent with infinitely many solutions.
                                    </div>
                                </div>
                            </details>
                        </div>
                    </div>
                </section>
            </div>
        </article>
        <div class="page-break"></div>
"""

print("Week 2 module loaded.")
